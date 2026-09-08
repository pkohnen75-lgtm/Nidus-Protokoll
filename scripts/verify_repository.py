"""Validate the archival manifest and navigation without executing source programs."""
from pathlib import Path
import hashlib,json,re,sys
from urllib.parse import unquote

root=Path(__file__).resolve().parents[1]
errors=[]
manifest=json.loads((root/'katalog/manifest.json').read_text(encoding='utf-8'))
documents=manifest['documents']; ids=[r['id'] for r in documents]
if len(ids)!=len(set(ids)): errors.append('Duplicate document IDs')
checks=0
for row in documents:
 for pathkey,hashkey in [('text_path','text_sha256'),('original_path','original_sha256'),('native_path','native_sha256')]:
  if pathkey not in row:continue
  path=(root/row[pathkey]).resolve()
  if not path.is_relative_to(root) or not path.is_file():errors.append('Missing or unsafe path: '+row[pathkey]);continue
  checks+=1
  if hashlib.sha256(path.read_bytes()).hexdigest()!=row[hashkey]:errors.append('Hash mismatch: '+row[pathkey])
 for rev in row.get('revision_history',[]):
  if not rev.get('path'):errors.append('Missing revision: '+row['id']+'/'+rev['id']);continue
  p=root/rev['path'];checks+=1
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=rev['sha256']:errors.append('Revision mismatch: '+str(p))
 card=root/row['record_path']
 if not card.is_file():errors.append('Missing document card: '+row['id'])
 meta=json.loads((root/'quellen'/row['id']/'metadaten.json').read_text(encoding='utf-8'))
 if meta!=row:errors.append('Metadata differs from manifest: '+row['id'])
linkcount=0
for md in root.rglob('*.md'):
 # Source copies may contain historical, broken or private links; verify authored navigation only.
 if md.is_relative_to(root/'quellen'):continue
 txt=md.read_text(encoding='utf-8')
 txt=re.sub(r'```.*?```','',txt,flags=re.S)
 for link in re.findall(r'\]\(([^)]+)\)',txt):
  link=link.strip('<>');link=unquote(link.split('#',1)[0])
  if not link or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link):continue
  linkcount+=1
  p=(md.parent/link).resolve()
  if not p.is_relative_to(root) or not p.exists():errors.append('Broken navigation: '+str(md.relative_to(root))+' -> '+link)
print(json.dumps({'documents':len(documents),'hash_checks':checks,'local_links':linkcount,'errors':errors},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
