#coding=utf-8
import cv2
import numpy as np
import Image
# img=cv2.imread('/home/zzq/py-faster-rcnn/data/VOCdevkit2007/VOC2007_back/JPEGImages/img_00003.jpg')
root='/home/zzq/kaggle/VOC2007/dest/'
dest='/home/zzq/dest/'
f=open('/home/zzq/鱼类的坐标')
lines=f.readlines()

for i in range(len(lines)):

	line_=lines[i].split()
	img_path=root+line_[0]

	img=np.array(Image.open(img_path))

	region=[]

	for j in range(2,6):
		region.append(int(line_[j]))
	# img_region=img[int(line_[2]):int(line_[5]),int(line_[3]):int(line_[4])]
	# img[int(line_[2]):int(line_[5]),int(line_[3]):int(line_[4])]=[255,255,255]
	for a in range(int(line_[2]),int(line_[5])):
		for b in range(int(line_[3]),int(line_[4])):
			img[a,b,:]=0
	# img_region=[255,255,255]
	# img.paste(img,region)
	raw_img_name=dest+'raw_'+line_[0]
	# img.save(raw_img_name)
	# cv2.imwrite(raw_img_name,img)
	new_im=Image.fromarray(img)
	new_im.save(raw_img_name)


