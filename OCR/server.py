#coding=utf-8
import BaseHTTPServer
import json
from ocr import OCRNN
import numpy as np 

host_name='localhost'
port_number=80
hidden_node_count=15

#load data sample and the labels
data_matrix=np.loadtxt(open('data.csv','rb'),delimiter=',')
data_labels=np.loadtxt(open('datalabels.csv','rb'))

#convert from numpy arrays to python lists
data_matrix=data_matrix.tolist()
data_labels=data_labels.tolist()

nn=OCRNN(hidden_node_count,data_matrix,datalabels,list(range(5000)))

class jsonhandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_post(s):
		response_code=200
		response=""
		var_len=int(s.headers.get('Content-Length'))
		content=s.rfile.read(var_len);
		payload=json.loads(content);
		if payload.get('train'):
			nn.train(payload['trainArray'])
			nn.save()
		elif payload.get('predict'):
			try:
				response={"type":"test","result":nn.predict(str(payload['image']))}
			except:
				response_code=500
		else:
			response_code=400

		s.send_response(response_code)
		s.send_headers("Content-type","application/json")
		s.send_headers("Access-Control-Allow-Origin","*")
		s.send_headers()
		if response:
			s.wfile.write(json.dumps(response))
		return 


if '__name__'=='__main__':
	server_class =BaseHTTPServer.BaseHTTPServer;
	httpd=server_class((host_name,port_number),jsonhandler)
	try:
		httpd.server_forever()
	except KeyboadInterrupt:
		pass
	else:
		print 'unkown server exception occured'
	finally:
		httpd.server_close()

