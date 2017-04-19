#coding=utf-8
import os
import Image
img=Image.open('/home/zzq/oceans17/figures/img1.jpg')
new_im=img.resize((640,360),Image.ANTIALIAS)
new_im.save('/home/zzq/resize.jpg')
		for k in range(len(li)):
			if j>=30 and k<=28:
				if(data[j-1][k]>20):
					data[j-1][k]*=0.3
				else:
					data[j-1][k]*=0.8