#!/usr/bin/python
def f(x):
	if(x>0):
		return x*x
	else:
		return x-1
print map(f,[1,-2,3])
