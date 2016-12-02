#coding=utf-8
import csv
import matplotlib.pyplot as pyt 
import matplotlib.cm as cm
import numpy as np 
from numpy import matrix
from collections import namedtuple
import math
import random
import json
import os

class OCRNN:
	lr=0.1
	width_in_pixel=20
	nn_file_path='nn.json'

	def __init__(self,num_hidden_nodes,data_matrix,data_labels,training_indices,use_file=True):
		self.sigmoid=np.vectorize(self._sigmoid_scalar)
		self.sigmoid_prime=np.vectorize(self.sigmoid_prime_scalar)
		self._usefile=use_file
		self.data_labels=data_labels
		self.data_matrix=data_matrix

		if (not os.path.isfile(OCRNN.nn_file_path) or not use_file):
			#step 1 initialize the weights to small numbers
			self.theta1=self._rand_initialize_weights(400,num_hidden_nodes)
			self.theta2=self._rand_initialize_weights(num_hidden_nodes,10)
			self.input_layer_bias=self._rand_initialize_weights(1,num_hidden_nodes)
			self.hidden_layer_bias=self._rand_initialize_weights(1,10)


			#train using the sample data
			train_data=namedtuple('train_data',['y0','label'])
			self.train(train_data[self.data_matrix[i],int(self.data_labels[i])] for i in training_indices)#使用列表生成式生成一堆数据然后再拿去训练
			self.save()

		else:
			self._load()


	def _rand_initialize_weights(self,size_in,size_out):
		return [((x*0.12)-0.06) for x in np.random.rand(size_out,size_in)]

	def _sigmoid_scalar(self,z):
		return 1/(1+math.e ** -z)#sigmoid 函数

	def _sigmoid_prime_scalar(self,z):
		return self.sigmoid(z)*(1-self.sigmoid(z))

	def _draw(self,sample):
		pixel_array=[sample[j:j+self.width_in_pixel] for j in xrange(0,len(sample),self.width_in_pixel)]
		pix_imshow(zip(*pixel_array),cmap=cm.Greys_r,interpolation="nearest")#最近邻插值
		plt.show()

	def train(self,train_data_array):
		for data in train_data_array:
			#前传
			y1=np.dot(np.mat(self.theta1),np.mat(data['y0']))#键值对,dot函数就是一个处理矩阵乘法的一个很好的优化好了的一个函数
			sum1=y1+np.mat(self.input_layer_bias)
			y1=self.sigmoid(sum1)

			y2=np.dot(np.array(self.theta2),y1)
			y2=np.add(y2,self.hidden_layer_bias)
			y2=self.sigmoid(y2)

			#后传
			actual_vals=[0]*10
			actual_vals[data['label']]=1
			output_errors=np.mat(actual_vals).T-np.mat(y2)

			hidden_errors=np.multiply(np.dot(np.mat(self.theta2).T,output_errors),self.sigmoid_prime(sum1))#计算数量积
			#update the weughts

			self.theta1+=self.lr*np.dot(np.mat(hidden_errors),np.mat(data['y0']))
			self.theta2+=self.lr*np.dot(np.mat(output_errors),np.mat(y1).T)#.T的意思是得到其转置
			self.hidden_layer_bias+=self.lr*output_errors
			self.input_layer_bias+=self.self.lr*hidden_errors

	def predict(self,test):
		y1=np.dot(np.mat(self.theta1),np.mat(test).T)
		y1=y1+np.mat(self.input_layer_bias)
		y1=self.sigmoid(y1)

		y2=np.dot(np.array(self.theta2),y1)
		y2=np.add(y2,self.hidden_layer_bias)
		y2=self.sigmoid(y2)

		results=y2.T.tolist()[0]
		return results.index(max(results))#取得最大值

	def save(self):
		if not self._usefile:
			return 
		json_neural_network={
		"theta1":[np_mat.tolist()[0] for np_mat in self.theta1],
		"theta2":[np_mat.tolist()[0] for np_mat in self.theta2],
		"b1":self.input_layer_bias[0].tolist()[0],
		"b2":self.hidden_layer_bias[0].tolist()[0]
		}
		with open(OCRNN.nn_file_path,"w") as nnfile:
			json.dump(json_neural_network,nnfile)#写入文件，json

	def _load(self):
		if not self._usefile:
			return

		with open(OCRNN.nn_file_path) as nnfile:
			nn=json.load(nnfile)
			self.theta1=[np.array(li) for li in nn['theta1']]
			self.theta2=[np.array(li) for li in nn['theta2']]
			self.input_layer_bias=[np.array(nn['b1'][0])]
			self.hidden_layer_bias=[np.array(nn['b2'][0])]


