#!/usr/bin/python
#coding:utf-8
def mysum(*args):
    return sum(args)
def myave(*args):
    return sum(args)/len(args)

def dec(func):
    def in_dec(*args):
        if len(args)==0:
            return 0
        for var in args:
            if not isinstance(val,int)
                return 0
        return func(*args)
    return in_dec
mysum = dec(mysum)
print (mysun(1,2,3))
