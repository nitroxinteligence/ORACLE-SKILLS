#!/usr/bin/env python3
"""Validador local de plano; não é um executor nem um controle imposto ao MCP.

O chamador fornece contexto verificado e aprovação real. SHA-256 associa a versão
do plano, mas não autentica quem aprovou. Nunca usar para fabricar consentimento.
Sem rede, subprocessos, credenciais ou mutações de contas/projetos.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ACTIONS = {'read', 'ads_write', 'local_edit', 'upload', 'paid_render', 'publish'}

def digest(plan: dict[str, Any]) -> str:
    raw=json.dumps(plan,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()

def stamp(value: str) -> datetime:
    if not isinstance(value,str): raise ValueError('Timestamp precisa ser string ISO.')
    d=datetime.fromisoformat(value.replace('Z','+00:00'))
    if d.tzinfo is None: raise ValueError('Timestamp sem fuso.')
    return d

def money(value: Any) -> Decimal:
    if isinstance(value,bool): raise ValueError('Booleano não é valor monetário.')
    try: d=Decimal(str(value))
    except (InvalidOperation,ValueError): raise ValueError('Valor monetário inválido.')
    if not d.is_finite() or d<0: raise ValueError('Valor monetário não finito ou negativo.')
    return d

def decide(plan: dict[str,Any], approval: dict[str,Any], context: dict[str,Any],
           now: str | None = None) -> dict[str,Any]:
    errors=[]
    if not all(isinstance(x,dict) for x in (plan,approval,context)):
        return {'allowed':False,'reasons':['schema_not_object']}
    try:
        plan_digest=digest(plan)
        current=stamp(now) if now else datetime.now(timezone.utc)
    except (TypeError,ValueError):
        return {'allowed':False,'reasons':['invalid_plan_or_time']}
    action=plan.get('action')
    if not isinstance(action,str):
        return {'allowed':False,'reasons':['action_must_be_string']}
    if action not in ACTIONS: errors.append('unsupported_action')
    if context.get('secrets_present') is True: errors.append('secret_material')
    if context.get('human_permission_prompt') is True: errors.append('human_permission_required')
    if context.get('instruction_injection') is True: errors.append('untrusted_instruction')
    target=plan.get('target')
    if not isinstance(target,str) or not target.strip(): errors.append('missing_target')
    if target!=context.get('verified_target'): errors.append('target_mismatch')
    if context.get('connected') is not True: errors.append('connection_not_verified')
    caps=context.get('capabilities',[])
    if not isinstance(caps,list) or action not in caps: errors.append('capability_missing')
    if action=='read':
        if context.get('read_authorized') is not True: errors.append('read_not_authorized')
    else:
        if context.get('read_only') is True: errors.append('read_only_executor')
        if approval.get('approved') is not True: errors.append('approval_missing')
        if approval.get('plan_sha256')!=plan_digest: errors.append('approval_for_different_plan')
        if approval.get('target')!=target: errors.append('approval_target_mismatch')
        if approval.get('action')!=action: errors.append('approval_action_mismatch')
        try:
            if stamp(approval.get('expires_at'))<=current: errors.append('approval_expired')
        except (TypeError,ValueError): errors.append('approval_expiry_invalid')
        used=context.get('consumed_approvals',[])
        if not isinstance(used,list): errors.append('invalid_consumed_approvals')
        elif plan_digest in used: errors.append('approval_already_consumed')
        if context.get('outcome_unknown') is True: errors.append('reconcile_before_retry')
        if plan.get('before_hash')!=context.get('current_state_hash') or not plan.get('before_hash'):
            errors.append('state_changed_or_unknown')
    if action in {'ads_write','paid_render'}:
        try:
            estimate=money(plan.get('max_cost'))
            ceiling=money(approval.get('max_cost'))
            if estimate>ceiling: errors.append('cost_above_approval')
        except ValueError: errors.append('cost_unknown_or_invalid')
        if not plan.get('currency') or plan.get('currency')!=context.get('currency') or plan.get('currency')!=approval.get('currency'):
            errors.append('currency_mismatch')
        if not plan.get('cost_period') or plan.get('cost_period')!=approval.get('cost_period'):
            errors.append('cost_period_mismatch')
    if action=='ads_write':
        if plan.get('create') is True and plan.get('new_status')!='PAUSED': errors.append('new_campaign_not_paused')
        if plan.get('activate') is True and approval.get('activation_authorized') is not True: errors.append('activation_not_authorized')
        if context.get('policy_review_ok') is not True: errors.append('provider_policy_not_verified')
    if action=='paid_render' and context.get('pending_job') is True: errors.append('existing_render_unresolved')
    if action=='upload':
        try:
            dest=urlsplit(plan.get('destination',''))
            hosts=context.get('approved_hosts',[])
            if not isinstance(hosts,list) or dest.scheme!='https' or not dest.hostname or dest.username or dest.password or dest.hostname not in hosts:
                errors.append('upload_destination_not_approved')
        except (TypeError,ValueError): errors.append('upload_destination_invalid')
        if approval.get('upload_authorized') is not True: errors.append('upload_not_authorized')
        files=plan.get('files')
        permitted=context.get('approved_files',[])
        if not isinstance(files,list) or not files or not isinstance(permitted,list) or any(f not in permitted for f in files):
            errors.append('upload_files_not_approved')
    if action=='local_edit':
        if context.get('working_copy_verified') is not True: errors.append('working_copy_missing')
        if context.get('gui') is True:
            if context.get('window_matches') is not True: errors.append('wrong_window')
            age=context.get('screenshot_age_seconds')
            # 30s é uma heurística local deste helper, não uma garantia do host.
            if isinstance(age,bool) or not isinstance(age,(int,float)) or not 0<=age<=30:
                errors.append('stale_or_missing_observation')
    if action=='publish':
        if approval.get('publication_authorized') is not True: errors.append('publication_not_authorized')
        if context.get('review_complete') is not True: errors.append('review_incomplete')
    return {'allowed':not errors,'reasons':errors,'plan_sha256':plan_digest,
            'boundary':'Validação local de dados; não autentica consentimento nem executa ferramentas.'}

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path,help='JSON sanitizado com plan, approval, context e now opcional.')
    args=parser.parse_args()
    try:
        payload=json.loads(args.input.read_text(encoding='utf-8'))
        result=decide(payload['plan'],payload.get('approval',{}),payload['context'],payload.get('now'))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        # Não imprimir o conteúdo da entrada nem trechos potencialmente sensíveis.
        result={'allowed':False,'reasons':['invalid_input'],'error_type':type(exc).__name__}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['allowed'] else 1

if __name__=='__main__': raise SystemExit(main())
