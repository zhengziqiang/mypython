#coding=utf-8
import Image  
import glob, os 
im=Image.open('/home/zzq/resize1.jpg')
new_im=im.rotate(225)
new_im.save('/home/zzq/demo2.jpg')