from pathlib import Path
import shutil, subprocess
root=Path(__file__).resolve().parent.parent
subprocess.run(['python3',str(root/'tools/build-episodes.py')],check=True)
out=root/'dist';out.mkdir(exist_ok=True)
for pattern in ['*.html','*.css','*.js','robots.txt','sitemap.xml']:
 for p in root.glob(pattern):shutil.copy2(p,out/p.name)
shutil.copytree(root/'assets',out/'assets',dirs_exist_ok=True)
print('Static build ready in dist/')
