import pandas as pd
import numpy as np


def readData():
    df = pd.read_csv("b.csv")    
    data = df.values
    
    N,M = data.shape
    newData = np.zeros((N,M+2))

    newCols = data[:,1]+1

    newData[np.arange(N), newCols.astype(np.int32)] = 1
    newData[:,0:1]= data[:,0:1]

    #print(data[2:5,0])
    #print(data[2:5,0:1])

    print(data[:,1])
   
    

readData()