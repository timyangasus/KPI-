import base64,re,sys,os
tpl,imgdir,out=sys.argv[1:4]
h=open(tpl,encoding='utf8').read()
def rep(m):
    p=os.path.join(imgdir,m.group(1)+'.jpg')
    return 'data:image/jpeg;base64,'+base64.b64encode(open(p,'rb').read()).decode()
h=re.sub(r'\{\{([\w-]+)\}\}',rep,h)
assert '{{' not in h
open(out,'w',encoding='utf8').write(h)
print(len(h)//1024,'KB')
