#!/usr/bin/python
def f():
	a,b=1,1
	while True:
		yield a
		a,b=b,a+b
for i in f():
	if i>100:
		break
	print i,
