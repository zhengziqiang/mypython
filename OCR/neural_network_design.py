import numpy as np
from ocr import OCRNN
from sklearn.cross_validation import train_test_split

def test(data_matrix,data_labels,test_indices,nn):
	avg_num=0
	for j in xrange(100):
		correct_guess_count=0
		for i in test_indices:
			test=data_matrix[i]
			prediction=nn.predict(test)
			if data_labels[i]==prediction:
				correct_guess_count+=1
		avg_num+=(correct_guess_count/float(len(test_indices)))
	return avg_num/100

data_matrix=np.loadtxt(open('data.csv','rb'),delimiter=',').tolist()
data_labels=np.loadtxt(open('datalabels.csv','rb')).tolist()

train_indices,test_indices=train_test_split(list(range(5000)))

print 'PERFORNANCE'
print '==========='

for i in xrange(5,50,5):
	nn=OCRNN(i,data_matrix,data_labels,train_indices,False)
	performance=str(test(data_matrix,data_labels,test_indices,nn))
	print '{i} hidden nodes:{val}'.format(i=i,val=performance) 
