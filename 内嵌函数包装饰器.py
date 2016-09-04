#!/usr/bin/python
#使用语法糖@来装饰函数
def demo(func):
    def _demo():
        print ("before my func called")
        func()
        print ("after my func called")
        #不需要返回func,实际上应该返回原函数的值
    return _demo
@demo
def myfunc():
    print ("myfunc called")
myfunc()
myfunc()
