#coding=utf-8
import Image  
import glob, os  
  
#图片批处理  
# def nofimage():  
#     for files in glob.glob('/home/zzq/kaggle/NoF/*.jpg'):  
#         filepath,filename = os.path.split(files)  
#         filterame,exts = os.path.splitext(filename)  
#         #输出路径  
#         opfile = r'/home/zzq/kaggle/nof_all/'  
#         #判断opfile是否存在，不存在则创建  
#         if (os.path.isdir(opfile)==False):
#             print 'not exist'  
#             os.mkdir(opfile)  
#         im = Image.open(files)  
#         #w,h = im.size  
#         #im_ss = im.resize((400,400))  
#         #im_ss = im.convert('P')
#         items=[45,90,135,180,225,270,315]
#         for item in items:
#             im_ss=im.rotate(item)
#             str_item=str(item)
#             #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
#             im_ss.save(opfile+filterame+str_item+'.jpg')  
def albimage():  
    for files in glob.glob('/home/zzq/kaggle/ALB/*.jpg'):  
        filepath,filename = os.path.split(files)  
        filterame,exts = os.path.splitext(filename)  
        #输出路径  
        opfile = r'/home/zzq/kaggle/alb_all/'  
        #判断opfile是否存在，不存在则创建  
        if (os.path.isdir(opfile)==False):
            print 'not exist'  
            os.mkdir(opfile)  
        im = Image.open(files)  
        #w,h = im.size  
        #im_ss = im.resize((400,400))  
        #im_ss = im.convert('P')
        items=[45,90,135,180,225,270,315]
        for item in items:
            im_ss=im.rotate(item)
            str_item=str(item)
            #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
            im_ss.save(opfile+filterame+str_item+'.jpg')  
def betimage():  
    for files in glob.glob('/home/zzq/kaggle/BET/*.jpg'):  
        filepath,filename = os.path.split(files)  
        filterame,exts = os.path.splitext(filename)  
        #输出路径  
        opfile = r'/home/zzq/kaggle/bet_all/'  
        #判断opfile是否存在，不存在则创建  
        if (os.path.isdir(opfile)==False):
            print 'not exist'  
            os.mkdir(opfile)  
        im = Image.open(files)  
        #w,h = im.size  
        #im_ss = im.resize((400,400))  
        #im_ss = im.convert('P')
        items=[45,90,135,180,225,270,315]
        for item in items:
            im_ss=im.rotate(item)
            str_item=str(item)
            #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
            im_ss.save(opfile+filterame+str_item+'.jpg')
def dolimage():  
    for files in glob.glob('/home/zzq/kaggle/DOL/*.jpg'):  
        filepath,filename = os.path.split(files)  
        filterame,exts = os.path.splitext(filename)  
        #输出路径  
        opfile = r'/home/zzq/kaggle/dol_all/'  
        #判断opfile是否存在，不存在则创建  
        if (os.path.isdir(opfile)==False):
            print 'not exist'  
            os.mkdir(opfile)  
        im = Image.open(files)  
        #w,h = im.size  
        #im_ss = im.resize((400,400))  
        #im_ss = im.convert('P')
        items=[45,90,135,180,225,270,315]
        for item in items:
            im_ss=im.rotate(item)
            str_item=str(item)
            #im_ss = im.resize((int(w*0.12), int(h*0.12)))  
            im_ss.save(opfile+filterame+str_item+'.jpg')  

if __name__=='__main__':
    print 'do'
    albimage()
    betimage()
    dolimage()
    #othertimage()
    print 'done'