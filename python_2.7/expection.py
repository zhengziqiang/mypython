import requests
from requests import exception

def build_url(endpoint):
    return '/'.join([url,endpoint])
def timeout():
	try:
		response=requests.get(build_url('user/email'),timeout=0.1)
		response.raise_for_status()
	except expectations.Timeout as e:
		print e.message
	except expectations.HTTPError as e:
		print e.message
	else:
		print response.text
		print response.status_code
def hard_request():
	from requests import Session,Request
	s=Session()
	headers={'User-Agent':'fake1.3.4'}
	req=Request('GET',build_url('user/emails'),auth=('imooc','imooc'),headers=headers)
	prepped=req.prepare()
	print prepped.body
	print prepped.headers

	resp= s.send(prepped,timeout=5)
	print resp.status_code
	print resp.request.headers
	print resp.text
if '__name__'=='__main__':
	timeout()