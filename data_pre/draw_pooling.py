#coding=utf-8
import numpy as np 
import cv2
import Image
dest='/home/zzq/dest/'
# size=14,14
lines=open('/home/zzq/log/pool/6').readlines()
for i in range(0,63):
	str_=lines[i*57]
	data=np.zeros((56,56))
	for j in range(1,57):
		# print lines[i*8+j]
		lin_=lines[i*57+j].split()
		# print type(lin_)
		li=[]
		for k in range(len(lin_)):
			# print type(lin_[k])
			li.append(float(lin_[k]))
		for k in range(len(li)):
			data[j-1][k]=li[k]
	new_im=Image.fromarray(data)
	new_im=new_im.convert('L')
	# dest_im=new_im.resize((28,28),Image.ANTIALIAS)
	dest_img_path=dest+'img_'+str(i)+'.jpg'
	new_im.save(dest_img_path)