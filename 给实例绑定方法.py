class Student(object):
	pass
def set_score(self,score):
	self.score=score
def get_score(self):
	return self.score
Student.set_score=set_score
Student.get_score=get_score
s=Student()
s.set_score(100)
print s.get_score()
