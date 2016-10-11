from urllib2 import Request ,HTTPError,URLError,urlopen
old_url='http://rrurl.cn/b1UZuP'
req=Request(old_url)
response=urlopen(req)
print 'old_url:'+old_url
print 'new_url:'+response.geturl()
