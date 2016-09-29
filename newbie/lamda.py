#!/usr/bin/python
f=lambda x,y,z:x+y+z
print (f(1,2,3))
l=[(lambda x:x**2),(lambda x:x**3),(lambda x:x**4)]
print l[0](2),l[1](2),l[2](2)
