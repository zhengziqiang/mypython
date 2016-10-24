#coding=utf-8
from PIL import Image
def encode_data_image(image,data):
	evenImage=make_image_even(image)
	binary=''.join(map(constLenBin,bytearray(data,'utf-8')))#将需要隐藏的文字转换为二进制字符串
	if len(binary) > len(image.getdata()) *4:
		raise Exception("Error: can't encode more than " + len(evenImage.getdata())) * 4 +""