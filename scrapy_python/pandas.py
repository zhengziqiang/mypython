#coding=utf-8
#通过引入一个csv文件来引入参数
import pandas as pd 
import csv
brics =pd.read_csv('/home/zzq/mypython/scrapy_python/data.csv')
print brics
print brics['country']
brics['on_earth']=[true,true]#添加一列数据
brics['destiny']=brics['population']/brics['area']*100000#进行类似于numpy的运算
brics.loc['BR']#以行的信息
brics.loc['BR','capital']#指定航标和列标
