#coding=utf-8
import os
import Image
  # 指定原始图片为问题所指路径
infile ="/home/zzq/kaggle/oceans17/figures/img.png"
# 修改输出扩展名为.jpeg
outfile = os.path.splitext(infile)[0] + ".jpg"
try:
  # 打开原始图像并存入新文件
  Image.open(infile).save(outfile)
  print "Covert to JPEG successfully!"
except IOError:
  # 错误处理
  print "This format can not support!", infile