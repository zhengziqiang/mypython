import pickle
d=dict(name='bob',age=20,score=80)
print pickle.dumps(d)
f=open("dump.txt",'wb')
pickle.dump(d,f)
f.close()
l=open('dump.txt','rb')
e=pickle.load(l)
l.close()
print e


import json
jd=dict(name='a')
json.dumps(jd)

