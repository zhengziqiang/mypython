#coding=utf-8
import sys,re
from handlers import *
from util import *
from rules import *

class Parser:
	#解析器父容器
	def __init__(self,handler):
		self.handler=handler
		self.rules=[]
		self.filters=[]
	def add_rule(self,rule):
		#添加规则
		self.rules.append(rule)

	def add_filter(self,pattern,name):
		#添加过滤器
		def filter(block,handler):
			return re.sub(pattern,handler.sub(name),block)
		self.filters.append(filter)
	def parse(self,file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters:
				block=filter(block,self.handler)
			for rule in self.rules:
				if rule.condition(block):
					last=rule.action(block,self.handler)
					if last:
						break
		self.handler.end('document')

class Basictextparser(Parser):
	#纯文本解析器
	def __init__(self,handler):
		Parser.__init__(self,handler)
		self.add_rule(Listrule())
		self.add_rule(Listitemrule())
		self.add_rule(Titlerule())
		self.add_rule(Headingrule())
		self.add_rule(Paragraphrule())
		self.add_filter(r'\*(.+?)\*', 'emphasis')
		self.add_filter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.add_filter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler=HTMLRender()
parser=Basictextparser(handler)
parser.parse(sys.stdin)