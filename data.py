import pandas as pd
import numpy as np

L = ['Tim',10,10,10,10,10,10,10,5,6,7,200,30,230] # this should create by the program

data = pd.read_csv('Data.csv')
data = data.drop(data.columns[0],axis=1)
newdata = data.append(pd.Series(L, index= data.columns),ignore_index=True)
# print(newdata)
newdata.to_csv('Data.csv')
# print(data)