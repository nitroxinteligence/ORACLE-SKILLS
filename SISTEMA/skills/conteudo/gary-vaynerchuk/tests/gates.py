"""Auxiliar de decisão puro: não acessa ferramentas, não publica e não impõe comportamento ao host."""
from typing import Any

MODES = {'context', 'research', 'audit', 'editorial', 'visual-brief', 'image', 'review', 'publish'}

def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise TypeError('Expected a dictionary.')
    mode = data.get('mode')
    if mode not in MODES:
        raise ValueError('Unknown workflow mode.')
    yes = lambda key: data.get(key) is True
    def result(status: str) -> dict[str, Any]:
        return {'status': status, 'publication_executed': False, 'tool_executed': False}
    if yes('private_export_requested'):
        return result('redact-context')
    if yes('unsupported_personal_claim'):
        return result('remove-unsupported-claims')
    if mode == 'context':
        return result('map-authorized-context' if yes('vault_access') else 'request-context')
    if mode == 'research':
        return result('research-ready' if yes('research_question') else 'clarify-research-scope')
    if mode == 'audit':
        if not yes('profile_material'): return result('request-profile-material')
        if not yes('audit_scope'): return result('clarify-audit-scope')
        return result('authorized-audit-ready' if yes('private_metrics') else 'public-audit-only')
    for key, status in [('context_validated','resolve-context'), ('brief_approved','approve-brief'), ('claims_supported','verify-claims')]:
        if not yes(key): return result(status)
    if mode == 'editorial': return result('editorial-draft-ready')
    if not yes('copy_approved'): return result('approve-copy')
    if mode == 'visual-brief': return result('visual-brief-ready')
    if mode == 'image':
        if not yes('visual_brief_approved'): return result('approve-visual-brief')
        if yes('is_edit') and not yes('edit_target_available'): return result('request-edit-target')
        if yes('user_portrait') and not yes('user_photo_available'): return result('request-user-photo')
        if not yes('generation_requested'): return result('brief-only')
        return result('image-operation-ready' if yes('image_tool') else 'generation-not-executed')
    if not yes('artifacts_available'): return result('request-artifacts')
    if yes('critical_defects'): return result('block-critical-defects')
    if mode == 'review': return result('review-ready')
    if not yes('final_review'): return result('require-final-review')
    if not yes('publication_authorized'): return result('require-publication-authorization')
    return result('authorized-publication-ready' if yes('publication_tool') else 'publication-not-executed')
