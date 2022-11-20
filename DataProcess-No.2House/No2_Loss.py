# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

#%% 

df1 = pd.read_csv('HO_Guest bathroom_Basin_Cold.csv')
df2 = pd.read_csv('HO_Guest bathroom_Basin_Hot.csv')
df3 = pd.read_csv('HO_Guest bathroom_Bathtub tap outlet_Mixed.csv')
df4 = pd.read_csv('HO_Guest bathroom_Movable shower head_Mixed.csv')
df5 = pd.read_csv('HO_Kitchen_Basin_Cold.csv')
df6 = pd.read_csv('HO_Kitchen_Basin_Hot.csv')
df7 = pd.read_csv('HO_Master bathroom_Basin_Cold.csv')
df8 = pd.read_csv('HO_Master bathroom_Basin_Hot.csv')
df9 = pd.read_csv('HO_Kitchen_Washing machine_Cold.csv')

y=[0,5,6,7,8,10,11,12,13,14]

df1.drop(df1.columns[y], axis=1, inplace=True)
df2.drop(df2.columns[y], axis=1, inplace=True)
df3.drop(df3.columns[y], axis=1, inplace=True)
df4.drop(df4.columns[y], axis=1, inplace=True)
df5.drop(df5.columns[y], axis=1, inplace=True)
df6.drop(df6.columns[y], axis=1, inplace=True)
df7.drop(df7.columns[y], axis=1, inplace=True)
df8.drop(df8.columns[y], axis=1, inplace=True)
df9.drop(df9.columns[y], axis=1, inplace=True)

frame1 = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9])
frame1.columns = ['sensor_id', 'gateway_id',
                  'latency_from_sensor_to_gateway',
                  'timestamp',
                  'latency_from_gateway_to_cloud']

frame1.to_csv('Useful_Data.csv',index = False)

#%%
frame1 = pd.read_csv('Useful_Data.csv')

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



