#coding=utf-8
import os
import Image
img=Image.open('/home/zzq/oceans17/figures/mask_raw.jpg')
new_im=img.resize((128,72),Image.ANTIALIAS)
new_im.save('/home/zzq/resize2.jpg')

