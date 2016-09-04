def demo(func):
	def _demo(*args,**kv):
		print ("before %s called"%func.__name__)
		ret =func(*args,**kv)
		print("after %s called result %s"%(func.__name__,ret))
		return ret
	return _demo
@demo
def myfunc(a,b):
	print("myfunc called (%s,%s)"%(a,b))
	return a+b
@demo
def myfunc2(a,b,c):
	print ("myfunc2 called(%s,%s,%s)"%(a,b,c))
	return a+b+c

myfunc(1,2)
myfunc2(1,2,3)