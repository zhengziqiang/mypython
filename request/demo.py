#coding=utf-8
import urllib#,urllib2
import urllib.request
url_ip='http://localhost/ip'
def use_simple_urllib():
    response=urllib.request.urlopen(url_ip)
    #print ">>>response header:"
    print (response.info())
    #print ">>>response.body()"
    print (''.join([line for line in response.readlines()]))
if __name__=='__main__':
    print ('use simple demo')
    use_simple_urllib()
