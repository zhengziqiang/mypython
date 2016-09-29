#!/usr/bin/python
def demo(func):
    print ("before myfunc called")
    func()
    print ("after myfunc called")
    return func

def myfunc():
    print ("my func called")
myfunc=demo(myfunc)
myfunc()
