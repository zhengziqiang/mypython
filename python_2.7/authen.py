#coding=utf-8
import requests
base_url='https://api.github.com'
def construct_url(end_point):
	return '/'.join([base_url,end_point])
def basic_auth():
	response=requests.get(construct_url('user'),auth=('imoocdemo','imoocdemo123'))
	print response.text
	print response.request.headers
	print 'basic auth'

def basic_oauth():
	headers={'Authorization':'token  '}
	response=requests.get(construct_url('user/email'),headers=headers)
	print response.request.headers
	print response.text
	print response.status_code
basic_auth()
from requests.auth import AuthBase

class github(AuthBase):
	def __init__(self,token):
		self.token=token
	def __call__(self,r):
		r.headers['Authorization']=' '.join(['token'],self.token)
		return r

def oauth():
	auth=github('  ')
	response=requests.get(construct_url('user/emails'),auth=auth)
	