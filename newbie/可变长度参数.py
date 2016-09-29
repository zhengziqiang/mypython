#!/usr/bin/python
def demo(*p):
	print p
print demo(1,2,3)
print demo(1,2,3,4,5,6)
def demo1(**q):
	for item in q.items():
		print (item),
print demo1(x=1,y=2,z=3)
