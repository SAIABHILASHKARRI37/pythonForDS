import os
dir=r"c:\vscode"
if not os.path.exists(dir):
    os.makedirs(dir)
info={}
info['mani']={'name':'mani','area':'kkd','ph':1234}
info['hari']={'name':'hari','area':'ppd','ph':5678}
import json
s=json.dumps(info)
with open("c://vscode//info.txt",'w') as f:
    f.write(s)

