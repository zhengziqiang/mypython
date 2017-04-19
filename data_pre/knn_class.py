import os
import operator

class knn_class():
	def __init__(self,k=3):
		self._k=k

	def _caledist(self,insample,dataset):
		m=dataset.shape[0]
		#np.tile函數,重複成（m,1)个维度的图形
		#重读样本个数多次
		diffmat=np.tile(insample,(m,1)) -dataset
		sqdiff=diffmat**2
		sqdistance=sqdiff.sum(axis=1)#求和
		distance=sqdistance ** 0.5 #开根号
		return distance.argsort()

	def _class(self,inx,dataset,labels):
		k=self._k
		datasize=dataset.shape[0]
		diffmat=np.tile(inx,(datasize,1)) -dataset
		sqdiff=diffmat**2
		sqdistance=sqdiff.sum(axis=1)
		distance=sqdistance**0.5
		sort_distance_index=distance.argsort()
		classcount={}
		for i in range(k):
			votelabel=labels[sort_distance_index[i]]
			classcount[votelabel]=classcount.get(votelabel,0)+1	