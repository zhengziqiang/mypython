#coding=utf-8
import urllib,urllib2
def use_simple_urllib():
    url_ip='http://localhost:8000/ip'
    response=urllib2.urlopen(url_ip)
 
    print '>>>response headers:'
    print response.info()
    print '>>response body:'
    print ''.join([line for line in response.readlines()])

def use_param_urllib():
    #构建请求参数
    param=urllib.urlencode({'param1':'hello','param2':'world'})
    print 'request param'
    print param
    response=urllib2.urlopen('?'.join([URL_GET,'%s'])%param)
    #处理响应
    print '>>>response headers:'
    print response.info()
    print '>>>status'
    print response.getcode()
    print '>>response body:'
    print ''.join([line for line in response.readlines()])


if __name__=='__main__':
    print 'use simple urllib2'
    use_simple_urllib()
    print 
    print 'use param urllib'
    use_param_urllib()
