import urllib2
from sgmllib import SGMLParser
class ListName(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_h4=""
		self.name=[]
	def start_h4(self,attrs):
		self.is_h4=1
	def end_4(self):
		self.is_h4=""
	def handle_data(self,text):
		if self.is_h4==1:
			self.name.append(text)

content=urllib2.urlopen("https://www.taobao.com/").read()
listname=ListName()
listname.feed(content)
for item in listname.name:
	print item.decode('gbk','ignore').encode('gbk')