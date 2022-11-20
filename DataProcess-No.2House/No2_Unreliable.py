#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:26:39 2020

@author: macbookpro
"""


import pandas as pd
import seaborn as sns

df = pd.read_csv('SystemProblem.csv')
p = pd.read_csv('ReliableData.csv')

print(df.shape)
print(p.shape)


#%%
#visionble the relationship between UnreliableData and device
df.info()  #更改
device_id_counts = df['sensor_id'].value_counts()
device_id_counts[:500]
subset =device_id_counts[:50]
print (subset)
ax = sns.barplot(y=subset.index, x=subset.values)
ax.set_xlabel("Number of Large Latency Occurred")
ax.set_ylabel("Suspicious Sensor ID")

#%%visionble the relationship between Usewater and Time

import csv
from datetime import datetime
from pandas import Series

file_name = 'All_latency.csv'  #更改
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    time = []
    for row in reader:
        current_time = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f')
        hour = current_time.hour
        time.append(hour)
        ser1 = Series(time)
        
p.info() #更改
hours_counts1 = ser1.value_counts()
hours_counts1[:500]
subset1 = hours_counts1[:5000]
print (subset1)
ax = sns.barplot(x=subset1.index, y=subset1.values)
ax.set_xlabel("Hour Scale of The Day")
ax.set_ylabel("Number of Using Water") 

#%%visionble the relationship between UnreliableData and Time

import csv
from datetime import datetime
from pandas import Series

file_name = 'SystemProblem.csv'   #更改
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    time,highs = [],[]
    for row in reader:
        current_time = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f')
        hour = current_time.hour
        time.append(hour)
        ser2 = Series(time)
        
df.info()  #更改
hours_counts2 = ser2.value_counts()
hours_counts2[:500]
subset2 = hours_counts2[:500]
print (subset2)
ax = sns.barplot(x=subset2.index, y=subset2.values)
ax.set_xlabel("Hour Scale of The Day")
ax.set_ylabel("Number of Large Latency Occurred")  
