# from PIL import Image
# im=Image.open('test.jpg')
# w,h=im.size
# print('Original image size %s * %s'%(w,h))
# im.thumbnail((w//2,h//2))
# im.save('thumbnail.jpg','jpeg')

#blur operation
# from PIL import Image,ImageFilter
# im=Image.open('test.jpg')
# im2=im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
def rngChar():
	return chr(random.randint(65,90))

def rngColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rngColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
font=ImageFont.truetype('/Library/Fonts/Arial.ttf',36)
draw=ImageDraw.Draw(image)
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rngColor())

for t in range(4):
	draw.text((60*t+10,10),rngChar(),font=font,fill=rngColor2())

image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')