"""Build index.html from src/ (single self-contained page; the field photo is inlined as base64).
Usage: python3 build.py   (needs Python 3 and, optionally, Node for the syntax check)"""
import base64, subprocess, shutil, os
d = os.path.dirname(os.path.abspath(__file__))
parts = ['p2.js', 'p3a.js', 'p3b.js', 'p3c.js', 'p3d.js', 'p4.js']
js = ''.join(open(f'{d}/src/{f}', encoding='utf-8').read() for f in parts)
b64 = base64.b64encode(open(f'{d}/assets/field.jpg', 'rb').read()).decode()
html = open(f'{d}/src/p1.html', encoding='utf-8').read() + '\n<script>\n' + js + '</script>\n'
open(f'{d}/index.html', 'w', encoding='utf-8').write(html.replace('__B64__', b64))
if shutil.which('node'):
    open('/tmp/_chk.js', 'w', encoding='utf-8').write(js.replace('__B64__', 'x'))
    print(subprocess.run(['node', '--check', '/tmp/_chk.js'], capture_output=True, text=True))
print('wrote index.html')
