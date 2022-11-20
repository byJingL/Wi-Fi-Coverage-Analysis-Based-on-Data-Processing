#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:26:39 2020

@author: macbookpro
"""


import pandas as pd

df = pd.read_csv('ReliableData.csv')
print(df.shape)

#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('ReliableData.csv')

cut=df.query('Total_latency<15000',inplace = False)

plt.hist(cut['Total_latency'], bins=70)
plt.show()

#%%
cut1v1= cut['Total_latency'].apply(np.log1p)

plt.hist(cut1v1, bins=70)
plt.show()

#%%
from scipy.stats import kstest

u = cut1v1.mean()
std = cut1v1.std()
testdata=kstest(cut1v1, 'norm',(u,std))

#%%
df.query('Total_latency>=8600',inplace = True)
df.to_csv('Large_latency.csv',index = False)
print(df.shape)

#%%
df['Time'] = pd.to_datetime(df['timestamp']) #将数据类型转换为日期类型

p1 = df[(pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')>= pd.to_datetime('2019-11-01',format = '%Y-%m-%d')) &
               (pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')<= pd.to_datetime('2020-01-22',format = '%Y-%m-%d'))]
p1.to_csv('All_latency1.csv',index = False)

p2 = df[(pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')>= pd.to_datetime('2020-01-22',format = '%Y-%m-%d')) &
               (pd.to_datetime(df['Time'] ,format = '%Y-%m-%d') <= pd.to_datetime('2020-02-07',format = '%Y-%m-%d'))]
p2.to_csv('All_latency2.csv',index = False)

p3 = df[(pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')>= pd.to_datetime('2020-02-07',format = '%Y-%m-%d')) &
               (pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')<= pd.to_datetime('2020-06-01',format = '%Y-%m-%d'))]
p3.to_csv('All_latency3.csv',index = False)

print(p1.shape)
print(p2.shape)
print(p3.shape)