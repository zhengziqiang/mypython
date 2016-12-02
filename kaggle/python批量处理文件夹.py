#coding=utf-8
from skimage import data_dir,io,transform,color
import numpy as np

def convert_gray(f):
     rgb=io.imread(f)    #依次读取rgb图片
     gray=color.rgb2gray(rgb)   #将rgb图片转换成灰度图
     dst=transform.resize(gray,(256,256))  #将灰度图片大小转换为256*256
     return dst
    
str=data_dir+'/*.png'
coll = io.ImageCollection(str,load_func=convert_gray)
for i in range(len(coll)):
    io.imsave('d:/data/'+np.str(i)+'.jpg',coll[i])  #循环保存图片