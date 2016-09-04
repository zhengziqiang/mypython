class Animal(object):
	def run():
		print "animal can run"
	def run_twice(animal):
		animal.run()
		animal.run()
class Dog(Animal):
	def run(self):
		print "dog can run"

class Cat(Animal):
	def run(self):
		print "cat can run"
dog=Dog()
dog.run()
cat=Cat()
cat.run()