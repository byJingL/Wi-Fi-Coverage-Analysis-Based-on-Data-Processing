#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:02:07 2020

@author: macbookpro
"""


import pandas as pd

#%% 
df1 = pd.read_csv('GuestBathroomBasinCold.csv')
df2 = pd.read_csv('GuestBathroomBasinHot.csv')
df3 = pd.read_csv('GuestBathroomBathtub.csv')
df4 = pd.read_csv('GuestBathroomFixedShowerHead.csv')
df5 = pd.read_csv('GuestBathroomMovableShowerHead.csv')
df6 = pd.read_csv('KitchenBasinCold.csv')
df7 = pd.read_csv('KitchenBasinHot.csv')
df8 = pd.read_csv('MasterBathroomBasinCold.csv')
df9 = pd.read_csv('MasterBathroomBasinHot.csv')
df10 = pd.read_csv('MasterBathroomBathtub.csv')
df11 = pd.read_csv('MasterBathroomMovableShowerHead.csv')
df12 = pd.read_csv('WashingMachine.csv')

x=[4,5,7,8]

df1.drop(df1.columns[x], axis=1, inplace=True)
df2.drop(df2.columns[x], axis=1, inplace=True)
df3.drop(df3.columns[x], axis=1, inplace=True)
df4.drop(df4.columns[x], axis=1, inplace=True)
df5.drop(df5.columns[x], axis=1, inplace=True)
df6.drop(df6.columns[x], axis=1, inplace=True)
df7.drop(df7.columns[x], axis=1, inplace=True)
df8.drop(df8.columns[x], axis=1, inplace=True)
df9.drop(df9.columns[x], axis=1, inplace=True)
df10.drop(df10.columns[x], axis=1, inplace=True)
df11.drop(df11.columns[x], axis=1, inplace=True)
df12.drop(df12.columns[x], axis=1, inplace=True)

#%% 

df13 = pd.read_csv('KS_Guest bathroom_Basin_Cold.csv')
df14 = pd.read_csv('KS_Guest bathroom_Basin_Hot.csv')
df15 = pd.read_csv('KS_Guest bathroom_Bathtub tap outlet_Mixed.csv')
df16 = pd.read_csv('KS_Guest bathroom_Fixed shower head_Mixed.csv')
df17 = pd.read_csv('KS_Guest bathroom_Movable shower head_Mixed.csv')
df18 = pd.read_csv('KS_Kitchen_Basin_Cold.csv')
df19 = pd.read_csv('KS_Kitchen_Basin_Hot.csv')
df20 = pd.read_csv('KS_Master bathroom_Basin_Cold.csv')
df21 = pd.read_csv('KS_Master bathroom_Basin_Hot.csv')
df22 = pd.read_csv('KS_Master bathroom_Bathtub tap outlet_Mixed.csv')
df23 = pd.read_csv('KS_Master bathroom_Movable shower head_Mixed.csv')
df24 = pd.read_csv('KS_Kitchen_Washing machine_Cold.csv')

y=[0,5,6,7,8,10,11,12,13,14]

df13.drop(df13.columns[y], axis=1, inplace=True)
df14.drop(df14.columns[y], axis=1, inplace=True)
df15.drop(df15.columns[y], axis=1, inplace=True)
df16.drop(df16.columns[y], axis=1, inplace=True)
df17.drop(df17.columns[y], axis=1, inplace=True)
df18.drop(df18.columns[y], axis=1, inplace=True)
df19.drop(df19.columns[y], axis=1, inplace=True)
df20.drop(df20.columns[y], axis=1, inplace=True)
df21.drop(df21.columns[y], axis=1, inplace=True)
df22.drop(df22.columns[y], axis=1, inplace=True)
df23.drop(df23.columns[y], axis=1, inplace=True)
df24.drop(df24.columns[y], axis=1, inplace=True)

frame1 = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,
                    df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24])
frame1.columns = ['sensor_id', 'gateway_id',
                  'latency_from_sensor_to_gateway',
                  'timestamp',
                  'latency_from_gateway_to_cloud']

frame1.to_csv('Original_Data.csv',index = False)