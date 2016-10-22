#coding =utf-8
import urllib
html=urllib.urlopen('https://en.wikipedia.org/wiki/National_Basketball_Association')
print html.read().decode(utf-8)
#文件输入进计算机是使用的是utf-8编码,而文件解码读取是使用的unicode编码,是为了更好的兼容，python3默认使用unicode编码，更加增强了对语言的兼容性，ansci编码不能识别的就是，
#不能识别的就是这样的方式 '\x'.decode(utf-8)