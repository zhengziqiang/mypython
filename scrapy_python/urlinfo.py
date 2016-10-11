from urllib2 import Request ,HTTPError,URLError,urlopen
old_url='http://www.baidu.com'
req=Request(old_url)
response=urlopen(req)
print 'info():'
print response.info()
