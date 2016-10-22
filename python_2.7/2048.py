import random
import os,sys
v=[[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]]

def display(v,score):
	print '%4d 	%4d	 %4d  %4d' %(v[0][0],v[0][1],v[0][2],v[0][3])
	print '%4d 	%4d	 %4d  %4d' %(v[0][0],v[0][1],v[0][2],v[0][3])
	print '%4d 	%4d	 %4d  %4d' %(v[0][0],v[0][1],v[0][2],v[0][3])
	print '%4d 	%4d	 %4d  %4d' %(v[0][0],v[0][1],v[0][2],v[0][3])
	print '\n'
	print 'total score %d'%score

def init(v):
	for i in range(4):
		v[i]=[random.choice([0,0,0,2,2,4]) for x in range(4)]


def align(vlist,direc):
	for i in range(vlist.count(0)):
		vlist.remove(0)
	zeros=[0 for  x in range(4-len(vlist))]
	if direc=='left':
		vlist.extend(zeros)
	else:
		vlist[:0]=zeros


def addsame(vlist,direc):
	score=0
	if direc=='left':
		for i in [0,1,2]:
			align(vlist,direc)
			if vlist[i]==vlist[i+1]!=0:
				vlist[i]*=2
				vlist[i+1]=0
				score+=vlist[i]
				return {'bool':True,'score':score}
	else:
		for i in [3,2,1]:
			align(vlist,direc)
			if vlist[i]==vlist[i+1]!=0:
				vlist[i]*=2
				vlist[i+1]=0
				score+=vlist[i]
				return {'bool':True,'score':score}
	return {'bool':False,'score':score}


def handle(vlist,direc):
	totalscore=0
	align(vlist,direc)
	result=addsame(vlist,direc)
	while result['bool']==True:
		totalscore+=result['score']
		align(vlist,direc)
		result=addsame(vlist,direc)
	result totalscore

def opera(v):
	totalscore=0
	gameover=False
	direc='left'
	op=raw_input()
