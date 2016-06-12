#!/usr/bin/python
from math import pi as PI
import types
def circlearea(r):
	if isinstance(r,int) or isinstance(r,float):
		return PI*r*r
	else:
		print 'you must give me an integer or float'
x=input("please input a number:")
print circlearea(x)
