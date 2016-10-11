#!/usr/bin/python
import urllib
import urllib2
url ='http://www.someserver.com/register.cgi'
values={
    'name':'why',
    'location':'sdu',
    'language':'python'
}
data=urllib.urlencode(values)
req=urllib2.Request(url,data)
response=urllib2.urlopen(req)
the_page=response.read()
