#!/usr/bin/env python3
"""Publish reviewed skills while retaining the immutable native baseline groups.

No vendor source is executed. Existing native review and package gates are reused.
"""
import argparse,copy,json,os,pathlib,re,stat
from oracle_distribution import audit_portability,canonical,decode,make_packages,read_stable,require,safe_path,sha,file_limit,MAX_FILES,MAX_BYTES,TEXT_EXTENSIONS,RESOURCE_EXTENSIONS,LICENSE_NAMES
from catalog_safety import check_publication_bytes
ROOT=pathlib.Path(__file__).resolve().parents[1]
def build(baseline,output,release_id,sequence):
 review=decode((ROOT/'publication-review.json').read_bytes());previous=decode((baseline/'manifest.json').read_bytes());require(sequence>previous['sequence'],'Catalog rollback refused')
 require(re.fullmatch(r'acervo-[0-9.]+',release_id),'Release identity invalid');require(not output.exists() and output.resolve()==output,'Fresh canonical output required')
 rows=[];blobs={};source_hashes={};known=set()
 for folder in ['SISTEMA/skills','SISTEMA/recursos-skills']:
  root=ROOT/folder;require(root.is_dir() and root.resolve()==root,'Public skill source absent')
  for parent,dirs,files in os.walk(root,followlinks=False):
   for name in dirs:require(not (pathlib.Path(parent)/name).is_symlink(),'Source links refused')
   for name in sorted(files):
    file=pathlib.Path(parent)/name;path=file.relative_to(ROOT).as_posix();safe_path(path,hidden=True)
    require(not any(p in {'.git','.env','.DS_Store','node_modules','.gbrain'} for p in pathlib.PurePosixPath(path).parts),'Private source metadata refused')
    info=file.lstat();require(stat.S_ISREG(info.st_mode) and info.st_nlink==1 and info.st_size<=file_limit(path),'Irregular or oversized source file')
    ext=file.suffix.lower().lstrip('.');require(not ext or ext in TEXT_EXTENSIONS|RESOURCE_EXTENSIONS or name.upper() in LICENSE_NAMES,'Unreviewed file format')
    key=path.lower();require(key not in known,'Portable path collision');known.add(key)
    data=read_stable(file,info);check_publication_bytes(path,data,review.get('publication_examples'));require(data[:2]!=b'MZ' and data[:4] not in [bytes.fromhex(x) for x in ['cffaedfe','feedfacf','cafebabe','7f454c46']],'Native file refused in skills')
    blobs[path]=data;source_hashes[path]=sha(data);rows.append({'path':path,'source_path':path,'kind':'specialists','size':len(data),'mode':493 if info.st_mode&0o111 else 420,'source_sha256':sha(data)})
 # The app's legacy prompts/tutorials and pinned source remain exactly signed.
 for old in previous['files']:
  if old['kind']=='specialists':continue
  file=baseline/'payload'/old['path'];before=file.lstat();require(file.resolve()==file and stat.S_ISREG(before.st_mode) and before.st_nlink==1 and before.st_size==old['size'] and before.st_size<=32000000,'Legacy baseline irregular');data=file.read_bytes();after=file.lstat();require(before.st_ino==after.st_ino and before.st_mtime_ns==after.st_mtime_ns and len(data)==old['size'] and sha(data)==old['sha256'],'Legacy baseline changed');blobs[old['path']]=data;rows.append({k:v for k,v in old.items() if k!='package_id'})
 vault_rows=[r for r in rows if r['kind']!='gbrain-source'];items,adaptations,problems=audit_portability(vault_rows,blobs,review)
 require(not problems,'Content review refused: '+json.dumps(problems[:12],ensure_ascii=True))
 required_licenses={r['path'] for r in review['licenses'] if isinstance(r,dict) and r.get('path')}
 discovered={r['path'] for r in vault_rows if pathlib.PurePosixPath(r['path']).name.upper().startswith(('LICENSE','LICENCE','COPYING'))}
 require(discovered<=required_licenses,'New license requires explicit publication review')
 for row in review['licenses']:
  if isinstance(row,dict) and row.get('path'):require(row['path'] in blobs and sha(blobs[row['path']])==row['sha256'],'Reviewed license changed')
 for row in rows:
  row.update(sha256=sha(blobs[row['path']]),size=len(blobs[row['path']]),item_ids=[i['id'] for i in items if row['path'] in i['required_files']],type='markdown' if row['path'].lower().endswith('.md') else 'resource')
 require(len(rows)<=MAX_FILES and sum(r['size'] for r in rows)<=MAX_BYTES,'Complete catalog exceeds supported budget')
 packages,payloads=make_packages(rows,blobs,release_id,'https://github.com/nitroxinteligence/ORACLE-SKILLS/releases/download/'+release_id)
 doc=copy.deepcopy(previous);doc.update(release_id=release_id,sequence=sequence,files=rows,packages=packages,items=items,inventory_sha256=sha(canonical(rows)),source_inventory_sha256=sha(canonical(source_hashes)),licenses=review['licenses'],adaptations=adaptations,publication_examples=review.get('publication_examples',{}),machine_path_reviews=review.get('machine_path_reviews',{}))
 doc['counts']={kind:{'files':sum(r['kind']==kind for r in rows),'bytes':sum(r['size'] for r in rows if r['kind']==kind),'items':sum(i['kind']=={'specialists':'skill','prompts':'prompt','tutorials':'tutorial'}.get(kind) for i in items)} for kind in sorted({r['kind'] for r in rows})}
 output.mkdir(mode=0o700,parents=True);(output/'manifest.json').write_bytes(canonical(doc))
 for name,data in payloads.items():(output/name).write_bytes(data)
 return {'files':len(rows),'skills':doc['counts']['specialists']['items'],'sequence':sequence,'releaseID':release_id,'legacyBaselinePreserved':True}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',required=True,type=pathlib.Path);p.add_argument('--output',required=True,type=pathlib.Path);p.add_argument('--release-id',required=True);p.add_argument('--sequence',required=True,type=int);a=p.parse_args();print(json.dumps(build(a.baseline.absolute(),a.output.absolute(),a.release_id,a.sequence)))
