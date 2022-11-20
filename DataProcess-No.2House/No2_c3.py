#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:34:41 2020

@author: macbookpro
"""

import pandas as pd
import seaborn as sns

#%%Obtain the Data in Third Period

df = pd.read_csv('ReliableData.csv')
df['Time'] = pd.to_datetime(df['timestamp']) 
p3 = df[(pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')>= pd.to_datetime('2020-02-07',format = '%Y-%m-%d')) &
               (pd.to_datetime(df['Time'] ,format = '%Y-%m-%d')<= pd.to_datetime('2020-06-01',format = '%Y-%m-%d'))]
p3.to_csv('All_latency3.csv',index = False)

print(p3.shape)

frame2 = pd.read_csv('Large_latency.csv')
frame2['Time'] = pd.to_datetime(frame2['timestamp']) 
period3 = frame2[(pd.to_datetime(frame2['Time'] ,format = '%Y-%m-%d')>= pd.to_datetime('2020-02-07',format = '%Y-%m-%d')) &
               (pd.to_datetime(frame2['Time'] ,format = '%Y-%m-%d')<= pd.to_datetime('2020-06-01',format = '%Y-%m-%d'))]
period3.to_csv('Large_latency3.csv',index = False)

print(period3.shape)

#%%
#visionble the relationship between Large_latency and device
period3.info()
device_id_counts = period3['sensor_id'].value_counts()
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

file_name = 'All_latency3.csv'  
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    time = []
    for row in reader:
        current_time = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f')
        hour = current_time.hour
        time.append(hour)
        ser1 = Series(time)
        
p3.info() 
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

file_name = 'Large_latency3.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    time,highs = [],[]
    for row in reader:
        current_time = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f')
        hour = current_time.hour
        time.append(hour)
        ser2 = Series(time)
        
period3.info()
hours_counts2 = ser2.value_counts()
hours_counts2[:500]
subset2 = hours_counts2[:500]
print (subset2)
ax = sns.barplot(x=subset2.index, y=subset2.values)
ax.set_xlabel("Hour Scale of The Day")
ax.set_ylabel("Frequency of High Latency Occurrence")  
