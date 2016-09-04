class Myobj(object):
	def __init__(self):
		self.__x=9
	def power(self):
		return self.__x	*self.__x
obj=Myobj()
print hasattr(obj,'x')
print hasattr(obj,'y')
setattr(obj,'y',9)
print isinstance(obj,Myobj)
print type(obj)