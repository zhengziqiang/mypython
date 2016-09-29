import os
print os.name
print (os.uname())
#print os.environ #check the environment of the os


print os.path.abspath(".")
os.mkdir("/home/zzq/mypython/test")# make a new directory
os.rmdir("/home/zzq/mypython/test")# delete a directory

os.path.split('/home/zzq/mypython/file.txt')
os.path.splitext('/home/zzq/mypython/file.txt')

os.rename('test.py','test1.py')#mv
os.remove('test1.py')#rm