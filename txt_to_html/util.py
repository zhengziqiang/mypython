#coding=utf-8
def lines(file):
	#生成器，在文本最后加1空行
	for line in file:yield file
	yield '\n'

def blocks(file):
	#生成器，生成独立的文本块
	block=[]
	for line in lines(file):
		if line.strip():#去除空格的一个函数
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block=[]
			
	#调用函数
