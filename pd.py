import pandas as pd
import numpy as np


def readData():
    df = pd.read_csv("mnn.csv")
    #print(df.head())
    #convert to numpy matrix
    data = df.values
    #print(data)
    #means 2D matrix with all the values except last 2rows and last 2columns
    X = data[2:6, -2:]
    #print(X)
    X = data[:, 3:4]
    #print(X.shape)
    X = data[2, -3]
    #print(X.shape) -not shape but value like int
    #print(X)
    print(data[0:2,0])
    Z = np.zeros((3,3))
    M= np.array([0, 1,0])
    print(M)
    Z[np.arange(3),M.astype(np.int32)]=1
    print(Z)
    #A, B = data.shape
    #print(A)
    #print(B)
    #creates a A*B 2D matrix initialized with 0
    #X2 = np.zeros((A,B))
    #X2[:,0:(B-1)] = data[:,0:(B-1)]
    #print(X2)
    #X2[:,:2] = X[:-4,:-2]
    #print(X2)
    #means matrix will all the values in 3rd column
    #Y = data[:, 3]
    #print(Y)
    

readData()