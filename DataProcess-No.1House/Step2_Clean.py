# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

#%%
frame1 = pd.read_csv('Original_Data.csv')

#check and delete null
a = pd.isnull(frame1).any().sum()
if a > 0 :
    cleaned = frame1.dropna()
    frame1 = cleaned
    print(a,'wrong data')
    
"""Step1 Calculate the All Latency"""
#%%
frame1.eval('Total_latency = latency_from_sensor_to_gateway + latency_from_gateway_to_cloud',
            inplace = True)
frame2 = frame1
frame2.to_csv('All_latency.csv',index = False)
print(frame2.shape)

"""Step2 Seprate the Data"""
#%%
SP=frame2.query('Total_latency>=1200000',inplace = False)
SP.to_csv('SystemProblem.csv',index = False)
print(SP.shape)

RD=frame2.query('Total_latency<1200000',inplace = False)
RD.to_csv('ReliableData.csv',index = False)
print(RD.shape)



