#coding=utf-8
class rule:
	def action(self,block,handler):
		#加标记
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True
class Headingrule(rule):
	#一号标题规则
	type='heading'
	def condition(self,block):
		#判断文本块是否符合规则
		return not '\n' in block and len(block) <=70 and not block[-1]== ':'
class Titlerule(Headingrule):
	#二号标题规则
	type='title'
	first =True
	def condition(self,block):
		if not self.first:
			return False
		self.first=False
		return Headingrule.condition(self,block);

class Listitemrule(rule):
	type='listitem'
	def condition(self,block):
		return block[0]=='-'
	def action(self,block,handler):
		handler.start(self.type)
		handler.feed(block[1:].strip())
		handler.end(self.type)
		return True

class Listrule(Listitemrule):
	#列表规则
	type='list'
	first=False
	def condition(self,block):
		return True
	def action(self,block,handler):
		if not 	self.inside and Listitemrule.condition(self,block):
			handler.start(self.type)
		elif self.inside and not  Listitemrule.condition(self,block):
			handler.end(self.type)
			self.inside=False
		return False

class Paragraphrule(rule):
	#段落规则
	type ='paragraph'
	def condition(self,block):
		return True
