f=open('/home/zzq/mypython/io/text','r')
print f.read()
f.close()

#with python 
with open('text','r') as f:#relative path is ok
	print (f.read())

#try mechanism
try:
	f=open('text','r')
	print f.read()
finally:
	if f:
		f.close()

t=open('lines','r')
for line in t.readlines():
	print (line.strip())

print 'write file input stream'
with open("write",'w') as w:
	w.write("hello world")