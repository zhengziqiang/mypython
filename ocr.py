#coding =utf-8
import csv
import matpotlib.pyplot as pyt 
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
