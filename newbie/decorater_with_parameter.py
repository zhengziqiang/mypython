def demo(func):
	def _demo(a,b):
		print ("before my func called")
		ret=func(a,b)
		print ("after my func called %s"%ret)
		return ret
	return _demo
@demo
def myfunc(a,b):
	print ("myfunc (%s,%s)"%(a,b))
	return a+b
myfunc(1,2)