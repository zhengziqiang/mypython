with open('demo.jpg','wb') as fd:
	for chunk in response.iter_content(128):
		fd.write(chunk)


import contextlib import closing
with closing(requests.get(url),headers =headers, stream=Ture) as response:
	with open('demo.jpg','wb') as fd:
		for chunk in response.iter_content(128):
			fd.write(chunk)


pip install 'requests[socksv5]'
proxies={'http':'sock5://127.0.0.1:1080','https':'sock5://127.0.0.1:1080'}

session是服务器端的
cookie是浏览器端的
http请求是带cookie的，解析cookie携带信息
cookies=dict(c='uid')
requests.get(url,cookies=cookies)