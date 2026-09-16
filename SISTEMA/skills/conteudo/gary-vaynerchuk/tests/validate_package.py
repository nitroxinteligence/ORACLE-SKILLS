"""Validação dirigida, somente leitura. Não prova integração Oracle nem eficácia de um modelo."""
from pathlib import Path
from urllib.parse import unquote
import json
import re
import sys
import yaml

ROOT=Path(__file__).resolve().parents[1]
VAULT=ROOT.parents[3]
REQUIRED={'id','type','status','area','created','updated','sensitivity','sources','confidence','review_after'}

def validate():
    errors=[]; links=0; notes=0
    manifest=json.loads((ROOT/'manifesto-skills.json').read_text())
    entries=manifest['skills']
    actual=list(ROOT.glob('gary-*/SKILL.md'))
    if len(entries)!=34 or len(actual)!=34: errors.append(f'Expected 34 skills, manifest={len(entries)}, actual={len(actual)}')
    for entry in entries:
        path=ROOT/entry['path']
        if not path.is_file(): errors.append('Missing skill: '+entry['path']); continue
        text=path.read_text()
        match=re.match(r'^---\n(.*?)\n---',text,re.S)
        if not match: errors.append('Missing frontmatter: '+str(path)); continue
        meta=yaml.safe_load(match[1])
        if meta.get('name')!=entry['slug']: errors.append('Incorrect name: '+entry['slug'])
        if not meta.get('description'): errors.append('Missing description: '+entry['slug'])
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',meta.get('name','')) or len(meta.get('name',''))>64: errors.append('Invalid name: '+entry['slug'])
        if not (path.parent/'references/indice.md').is_file(): errors.append('Missing reference map: '+entry['slug'])
    source_files=list((ROOT/'references/fontes').glob('*.md'))
    role_files=[p for p in (ROOT/'agents').glob('*.md') if p.stem!='indice']
    if len(source_files)!=49: errors.append('Expected 49 source cards')
    if len(role_files)!=14: errors.append('Expected 14 role contracts')
    for path in ROOT.rglob('*.md'):
        text=path.read_text(encoding='utf-8')
        if path.name not in {'SKILL.md','AGENTS.md'}:
            match=re.match(r'^---\n(.*?)\n---',text,re.S)
            if not match: errors.append('No note frontmatter: '+str(path.relative_to(ROOT)))
            else:
                try:
                    meta=yaml.safe_load(match[1]); missing=REQUIRED-set(meta)
                    if missing: errors.append(f'{path.relative_to(ROOT)} missing fields {sorted(missing)}')
                except Exception as exc: errors.append(f'YAML error {path}: {exc}')
            notes+=1
        for target in re.findall(r'\[\[([^\]]+)\]\]',text):
            target=target.split('|')[0].split('#')[0]
            if not target: continue
            resolved=VAULT/target
            links+=1
            if not resolved.exists() and not resolved.with_suffix('.md').exists(): errors.append(f'{path.relative_to(ROOT)} broken wiki: {target}')
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
            if target.startswith(('http:','https:','mailto:','#')): continue
            target=unquote(target.split('#')[0]).strip('<>')
            if not target: continue
            links+=1
            resolved=path.parent/target
            if not resolved.exists(): errors.append(f'{path.relative_to(ROOT)} broken relative link: {target}')
    result={'scope':'Native vault package: structure and link existence, not semantic truth, LLM behavior or app integration.','skills':len(actual),'role_contracts':len(role_files),'source_cards':len(source_files),'notes_checked':notes,'local_links_checked':links,'errors':errors,'passed':not errors}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not errors else 1

if __name__=='__main__': sys.exit(validate())
