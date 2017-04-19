def demo(arg):
	def _demo(func):
		def __demo():
			print ("before %s called [%s]"%(func.__name__,arg))
			func()
			print ("after %s called [%s]"%(func.__name__,arg))
			return __demo
		return _demo

@demo("mymodule")
def myfunc():
	print ("myfunc called")
@demo("mymodule2")
def myfunc2():
	print ("myfunc2")

myfunc()
myfunc2()