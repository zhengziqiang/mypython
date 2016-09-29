class Animal(object):
	pass
class Dog(Animal):
	pass
class Runable(object):
	def run(self):#self is needed
		print 'I can run'
class Dog(Animal,Runable):
	pass
dog=Dog()
dog.run()