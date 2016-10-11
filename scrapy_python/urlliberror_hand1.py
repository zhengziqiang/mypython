from urllib2 import Request,urlopen,URLError,HTTPError
req=Request('http://bbs.csdn.net/callmewhy')
try:
    response=urlopen(req)
except HTTPError,e:
    print 'the error couldn\'t fullfil the request'
    print 'error code',e.code
except URLError,e:
    print 'we failed to reach a server'
    print 'reason',e.reason
else:
    print 'no exception was failed'
