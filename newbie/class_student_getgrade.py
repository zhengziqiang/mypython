class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print ("%s:%s"%(self.name,self.score))
	def get_grade(self):
		if self.score>=90:
			return 'A'
		elif self.score>=80:
			return 'B'
		else:
			return 'False'
bart=Student('Bart',59)
bart.print_score()
b=bart.get_grade()
print b