import fs from 'node:fs/promises';import {resolve,join,dirname} from 'node:path';
import {latestRelease,releaseBytes} from '../packages/oracle-desktop-portable/release-network.mjs';
import {loadReviewedContentTrust} from '../packages/oracle-desktop-portable/content-admission.mjs';
import {admitSkillsRelease,skillsSHA,skillsBase64,verifySkillsFile} from '../packages/oracle-desktop-portable/skills-release-admission.mjs';
const output=resolve(process.argv[2]||'');if(!process.argv[2]||await fs.realpath(dirname(output))!==dirname(output))throw Error('Fresh canonical baseline required');await fs.mkdir(output,{mode:0o700});
const release=await latestRelease('nitroxinteligence/ORACLE-SKILLS'),asset=release.assets.find(r=>r.name==='oracle-distribution.json');
if(!asset||asset.size>24000000||!/^sha256:[a-f0-9]{64}$/.test(asset.digest??''))throw Error('Signed latest catalog required');
const bytes=await releaseBytes(asset.browser_download_url,{maximum:24000000,expectedBytes:asset.size});if('sha256:'+skillsSHA(bytes)!==asset.digest)throw Error('Catalog asset changed');
const admitted=admitSkillsRelease(bytes,{trust:loadReviewedContentTrust()}),doc=JSON.parse(skillsBase64(JSON.parse(bytes).payload_base64));if(doc.release_id!==release.tag_name)throw Error('Catalog tag changed');
await fs.writeFile(join(output,'manifest.json'),JSON.stringify(doc),{flag:'wx'});await fs.writeFile(join(output,'envelope.json'),bytes,{flag:'wx'});
const inventory=new Map(doc.files.map(r=>[r.path,r]));let count=0;
for(const pkg of doc.packages){
 const data=await releaseBytes(pkg.url,{maximum:pkg.bytes,expectedBytes:pkg.bytes});if(skillsSHA(data)!==pkg.sha256)throw Error('Catalog package changed');const value=JSON.parse(data);if(value.id!==pkg.id||value.release_id!==doc.release_id||value.files.length!==pkg.files.length)throw Error('Package identity changed');
 const seen=new Set();for(const r of value.files){const row=inventory.get(r.path),file=skillsBase64(r.content_base64);if(!row||seen.has(r.path)||row.package_id!==pkg.id||file.length!==row.size||skillsSHA(file)!==row.sha256||r.mode!==row.mode||r.sha256!==row.sha256)throw Error('Catalog file changed');seen.add(r.path);if(row.kind==='specialists')verifySkillsFile(admitted,r.path,file);const target=join(output,'payload',r.path);await fs.mkdir(dirname(target),{recursive:true});await fs.writeFile(target,file,{flag:'wx',mode:row.mode});count++;}
}
if(count!==doc.files.length)throw Error('Incomplete signed baseline');console.log(JSON.stringify({signatureVerified:true,sequence:doc.sequence,files:count}));
