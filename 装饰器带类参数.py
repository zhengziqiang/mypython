class locker:
	def __init__(self):
		print ("locker.__init__() should be not called")
	@staticmethod
	def acquire():
		print ("this is locker.acquire ()called")
	@staticmethod
	def release():
		print ("locker.release() callled")

def demo(cls):
	def _demo(func):
		def __demo():
			print("before %s called [%s]."%(func.__name__,cls))
			cls.acquire()
			try:
				return func()
			finally:
				cls.release()
		return __demo
	return _demo

@demo(locker)
def myfunc():
	print ("myfunc called")
myfunc()
myfunc()