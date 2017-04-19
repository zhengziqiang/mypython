import numpy as np 
class kmeans():
	def __init__(self,k=3,initcent='random',max_iter=500):
		self._k=k 
		self._initcent=initcent
		self._max_iter=max_iter
		self._cluster=None
		self._labels=None
		self._sse=None

	def _calEdit(self,arra,arrb):
		return np.math.sqrt(sum(np.power(arra-arrb,2)))

	def _calMdist(self,arra,arrb):
		return sum(np.abs(arra-arrb))

	def _randcent(self,data,k):
		n=data.shape[1]
		centroids=np.empty((k,n))
		for j in range(n):
			minj=min(data[:,j])
			rangej=float(max(data[:,j]-minj))
			centroids[:,j]=(minj+rangej*np.random.rand(k,1)).flatten()
		return centroids

	def fit(self,data):
		if not isinstance(data,np.ndarray) or isinstance(data,np.matrixlib.defmatrix.matrix):
			try:
				data=np.asarray(data)
			except:
				raise TypeError("numpy.ndarray required for data")

		m=data.shape[0]
		self._cluster=np.zeros((m,2))
		if self._initcent=='random':
			self._centroids=self._randcent(data,k)
		cluster_change=False
		for _ in range(max_iter):

			#just a loop 
			for i in range(m):
				mindist=np.inf
				mindex=-1
				for j in range(self._k):
					arra=self._centroids[j,:]
					arrb=data[i,:]
					dist=self._calEdit(arra,arrb)
					if dist<mindist:
						mindist=dist
						mindex=j
				if self._cluster[i,0]!=mindex:
					cluster_change=True
					self._cluster[i,:]=mindex,mindist**2
