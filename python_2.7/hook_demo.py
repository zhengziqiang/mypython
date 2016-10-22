#coding=utf-8
import requests
def get_key(response,*args,**kwargs):
	print '回调函数'
	print response.headers['Content-Type']
def main():
	response=requests.get('http://www.baidu.com',hooks=dict(response=get_key))

main()