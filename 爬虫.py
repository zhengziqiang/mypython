#!/usr/bin/python
#coding:utf-8
import urllib2
url1='http://www.baidu.com'
print '第一种方法'
response1=urllib2.urlopen(url1)
print response1.getcode()
print len(response1.read())


print response1.read()
