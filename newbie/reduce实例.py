#!/usr/bin/python
from functools import reduce
def fn(x,y):
    return x*10+y
m=reduce(fn,[1,3,5,7,9])
print m
