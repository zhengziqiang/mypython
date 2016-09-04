class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object(name: %s)'%self.name

class fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
