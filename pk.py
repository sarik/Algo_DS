import pandas as pd
import numpy as np


def readData():
    df = pd.read_csv("b.csv")    
    data = df.values
    N,M = data.shape
    newData = np.zeros((N,M+2))

    colsToModify = data[:,1]
    print(colsToModify[:-1])
    newData[np.arange(7), colsToModify[:-1]+1] = 1
    newData[:,0] = data[:,0]    
    print(newData)
   
    

readData()

S= np.random.randn(3,4)
T= np.random.randn(3)

print(S)
print(T)

print(S[T>0.1])