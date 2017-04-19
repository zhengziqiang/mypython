#coding=utf-8
 
import numpy as np
from PIL import Image
import glob,os
root='/home/zzq/3/'
data=np.zeros((356,356))
new_im=Image.fromarray(data)
new_im=new_im.convert('L')
lines=open('/home/zzq/3/log','r').readlines()
for i in range(6):
	for j in range(6):
		region=[]
		region.append(j*56+j*4)
		region.append(i*60)
		region.append(j*60+56)
		region.append(i*60+56)
		line_=lines[i*6+j].strip('\n')
		img_path=root+line_
		print img_path
		print region
		Img=Image.open(img_path)
		new_im.paste(Img,region)
new_im.save('/home/zzq/merge_2.jpg')