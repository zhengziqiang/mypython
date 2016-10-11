from urllib2 import Request ,urlopen, HTTPError, URLError
req=Request('http://bbs.csdn.net/callmewhy')
try:
    response=urlopen(req)
except URLError,e:
    if hasattr(e,'code'):
        print 'there are some codes',e.code
    elif(e,'reason'):
        print 'the reason is ',e.reason
    else:
        print "there are nothing"

