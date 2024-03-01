import os
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib import animation, rc
rc('animation', html='jshtml')
import folium
from folium import plugins
from folium.features import PolyLine

data=pd.read_csv('/Users/mac/Desktop/Python/src/datascience/abddata.csv')
data=data.iloc[:,1:]
for i in range(len(data)):
    if '/' in data.loc[i,'Date']:
        d,m,y=data.loc[i,'Date'].split('/')
        data.loc[i,'Date']=y+'-'+m.zfill(2)+'-'+d.zfill(2)
print(data['Date'])

for i in range(len(data)):
    try:
        data.loc[i,'Date'] = pd.to_datetime(data.loc[i, 'Date'])
    except:
        print(i, data.loc[i, 'Date'])
print(data['Date'])

cols0=data.columns.tolist()
cols=[]
for col in cols0:
    if '_Price' in col:
        cols+=[col]
print(cols)

cols2=[]
for col in cols:
    if data[col].dtype==np.float64:
        cols2+=[col]
print(cols2)

cols3=list(set(cols)-set(cols2))
print(cols3)

data[cols2].info()

for col in cols2:
    plt.figure(figsize=(11,4))
    plt.plot(data['Date'], data[col], marker='o', markersize=3) 
    plt.xlabel('Date')
    plt.ylabel(col)
    plt.xticks(rotation=45)
    plt.title(col)
    plt.show()