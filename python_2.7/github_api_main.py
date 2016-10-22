#coding=utf-8
import json,requests
url='https://api.github.com'
def build_url(endpoint):
    return '/'.join([url,endpoint])
def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)
def request_method():
	response=requests.get(build_url('users/imoocdemo'))#demo
	response=requests.get(build_url('user/email'),auth=('imoocdemo','imoocdemo123'))#将密码明文发送
	print better_print(response.text)

def param_request():
	response=requests.get(build_url('users'),params={'since':11})
	print better_print(response.text)
	print response.request.headers
	print response.url

def json_request():
	response=requests.patch(build_url('user'),auth=('imoocdemo','imoocdemo123'),json={'name':'babyimooc2','email':'hello-world@imooc.org'})
	response=requests.post(build_url('user/email'),auth=('imoocdemo','imoocdemo123'))
	print better_print(response.text)
	print response.request.headers
	print response.request.body
	print response.status_code
if __name__=='__main__':
	#request_method()
	#param_request()
	json_request()


