#!/usr/bin/python
def Join(list,sep=None):
	return (sep or ' ').join(list)
list=['a','b','c']
print Join(list)
print Join(list,',')
