#coding=utf-8
#中文
import numpy as np 
height=[175,180,178]
weight=[67,78,76]
np_height=np.array(height)
np_weight=np.array(weight)
bmi=np_weight/np_height**2
list_=np_height+np_weight
for x in bmi:
	print x
for y in list_:
	print y
print list_[2]
bmi>254
list_>254
print list_
print list_[list_>254]#起到选择数据的作用，只能有一个类型的数据p
np_2d=np.array([[1,2,3,4,5],
	[2,3,4,5,6]])
print np_2d[1,2]
print np_2d[:,1:3]
print np.mean(np_weight)#求出平均数
print np.median(np_weight)#求出中位数
print np.corrcoef(np_weight,np_height)#检验这两个数据有没有相干性

print np.std(np_height)#求得标准差
#np.round(np.random.normal(1.75,0.2,5000),2)生成500个数据
#np.column_stack((height,weight))通过列连接