#!/usr/bin/env python3
import argparse,datetime,hashlib,json,os,pathlib,subprocess,tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
def run(args,env=None):
 p=subprocess.run(list(map(str,args)),cwd=ROOT,env=env or os.environ.copy(),capture_output=True,text=True)
 if p.returncode:
  print(p.stderr[-4000:],flush=True);raise subprocess.CalledProcessError(p.returncode,p.args)
 if p.stdout.strip():print(p.stdout[-2500:],flush=True)
 return p.stdout
def main(a):
 secret=os.environ.pop('ORACLE_DISTRIBUTION_KEY',None);token=os.environ.pop('GH_TOKEN',None) or os.environ.pop('GITHUB_TOKEN',None)
 if not secret:raise ValueError('Scoped signing secret required')
 (ROOT/'.work').mkdir(exist_ok=True);job=pathlib.Path(tempfile.mkdtemp(prefix='skills-release-',dir=ROOT/'.work'));baseline=job/'baseline';run(['node','scripts/download-catalog-baseline.mjs',baseline]);previous=json.loads((baseline/'manifest.json').read_text())
 state=ROOT/'publication-state.json';pending=json.loads(state.read_text())['sequence'] if state.exists() else 0
 sequence=max(previous['sequence'],pending)+1;release='acervo-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y.%m.%d')+'.'+str(sequence);stage=job/'candidate'
 run(['python3','scripts/build-skills-release.py','--baseline',baseline,'--output',stage,'--release-id',release,'--sequence',sequence])
 signing_root=pathlib.Path(os.environ.get('RUNNER_TEMP',tempfile.gettempdir())).resolve()
 if signing_root.is_relative_to(ROOT):raise ValueError('External signing directory required')
 fd,key_path=tempfile.mkstemp(prefix='oracle-catalog-',suffix='.pem',dir=signing_root)
 try:
  os.fchmod(fd,0o600)
  with os.fdopen(fd,'w') as file:file.write(secret)
  run(['node','scripts/sign-skills-release.mjs',stage,key_path])
 finally:pathlib.Path(key_path).unlink(missing_ok=True)
 assets=[stage/'oracle-distribution.json',*sorted(stage.glob('specialists-*.json')),*sorted(stage.glob('prompts-*.json')),*sorted(stage.glob('tutorials-*.json')),*sorted(stage.glob('gbrain-source-*.json'))]
 sums=stage/'SHA256SUMS';sums.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in assets));assets.append(sums)
 if a.mode=='validate':print(json.dumps({'qualified':True,'published':False,'releaseID':release,'output':str(stage)}));return
 if not token:raise ValueError('Scoped own repository token required')
 publish_env={**os.environ,'GH_TOKEN':token};state.write_text(json.dumps({'sequence':sequence,'releaseID':release,'manifestSHA256':hashlib.sha256((stage/'oracle-distribution.json').read_bytes()).hexdigest()},indent=2)+'\n')
 run(['git','config','user.name','oracle-skills-release']);run(['git','config','user.email','oracle-skills-release@users.noreply.github.com']);run(['git','add','publication-state.json']);run(['git','commit','-m','Publish reviewed catalog '+release+' [skip ci]']);run(['git','tag',release]);run(['gh','auth','setup-git'],env=publish_env);run(['git','push','--atomic','origin','HEAD:main','refs/tags/'+release],env=publish_env)
 notes=job/'notes.md';notes.write_text('Acervo assinado, completo e revisado. Atualiza skills e recursos, preservando notas editadas no vault. Os grupos legados do aplicativo nativo permanecem no inventário com os bytes publicados anteriormente.\n')
 run(['gh','release','create',release,*assets,'--draft','--verify-tag','--title','Acervo Oracle '+release,'--notes-file',notes],env=publish_env);run(['gh','release','edit',release,'--draft=false','--latest'],env=publish_env);print(json.dumps({'qualified':True,'published':True,'releaseID':release,'sequence':sequence}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['release','validate'],default='release');main(p.parse_args())
