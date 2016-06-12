#!/usr/bin/python
class root:
	__total=0
	def __init__(self,v):
		self.__value=v
		root.__total+=1
	def show(self):
		print ('self.__value:',self.__value)
		print ('root.__total:',root.__total)
	@classmethod
	def classshowtotal(cls):
		print (cls.__total)
	@stati
