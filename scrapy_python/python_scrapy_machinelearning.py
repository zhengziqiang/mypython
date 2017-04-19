#coding=utf-8
import re
import urllib
def gethtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	print 'read done'
	return html
def get_mp4(html):
	r=r"href='(http.\*.mp4)'"
	re_mp4=re.compile(r)
	mp4_list=re.findall(re_mp4,html)
	filename=1
	for mp4url in mp4_list:
		urllib.urltrieve(mp4url,"%s.mp4"%filename)
		print 'file "%s.mp4" ' %filename
		filename+=1
url=raw_input("please input the source url:")
gethtml(url)
get_mp4(html)