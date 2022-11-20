#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:32:26 2020

@author: macbookpro
"""

import pandas as pd
import seaborn as sns

#%%Obtain the Data in First Period

df = pd.read_csv('ReliableData.csv')
df['Time'] = pd.to_datetime(df['timestamp'])
p1 = df[(pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')>= pd.to_datetime('2019-11-01',format = '%Y-%m-%d')) &
               (pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')<= pd.to_datetime('2020-01-22',format = '%Y-%m-%d'))]
p1.to_csv('All_latency1.csv',index = False)
print(p1.shape)

frame2 = pd.read_csv('Large_latency.csv')
frame2['Time'] = pd.to_datetime(frame2['timestamp'])
period1 = frame2[(pd.to_datetime(frame2['Time'] ,format = '%Y-%m-%d')>= pd.to_datetime('2019-11-01',format = '%Y-%m-%d')) &
               (pd.to_datetime(frame2['Time'] ,format = '%Y-%m-%d')<= pd.to_datetime('2020-01-22',format = '%Y-%m-%d'))]
period1.to_csv('Large_latency1.csv',index = False)
print(period1.shape)


#%%
#visionble the relationship between Large_latency and device
period1.info()
device_id_counts = period1['sensor_id'].value_counts()
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

file_name = 'All_latency1.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    time = []
    for row in reader:
        current_time = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f')
        hour = current_time.hour
        time.append(hour)
        ser1 = Series(time)
        
p1.info()
hours_counts1 = ser1.value_counts()
hours_counts1[:500]
subset1 = hours_counts1[:5000]
print (subset1)
ax = sns.barplot(x=subset1.index, y=subset1.values)
ax.set_xlabel("Hour Scale of The Day")
ax.set_ylabel("Frequency of Water Consumption") 

#%%visionble the relationship between Large_latency and Time

import csv
from datetime import datetime
from pandas import Series

file_name = 'Large_latency1.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    time,highs = [],[]
    for row in reader:
        current_time = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f')
        hour = current_time.hour
        time.append(hour)
        ser2 = Series(time)
        
period1.info()  #更改
hours_counts2 = ser2.value_counts()
hours_counts2[:500]
subset2 = hours_counts2[:500]
print (subset2)
ax = sns.barplot(x=subset2.index, y=subset2.values)
ax.set_xlabel("Hour Scale of The Day")
ax.set_ylabel("Frequency of High Latency Occurrence")  

