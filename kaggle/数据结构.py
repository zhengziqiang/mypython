#coding=utf-8
import pandas as pd
with pd.HDFStore("/home/zzq/kaggle/train.h5","r") as train:
	df=train.get("train")
print len(df)
