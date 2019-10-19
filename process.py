import numpy as np
import pandas as pd
import os

# so scripts from other folders can import this file
dir_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

# normalize numerical columns
# one-hot categorical columns

def get_data():
  df = pd.read_csv(dir_path + '/ecommerce_data.csv')

  # just in case you're curious what's in it
  # df.head()

  # easier to work with numpy array
  data = df.values
  #print(data[1,-1:])
  
  # shuffle it
  np.random.shuffle(data)
  #print(data[1:2,-1:])

  # split features and labels
  X = data[:,:-1]
  Y = data[:,-1].astype(np.int32)

  # one-hot encode the categorical data
  # create a new matrix X2 with the correct number of columns
  N, D = X.shape
  X2 = np.zeros((N, D+3))
  X2[:,0:(D-1)] = X[:,0:(D-1)] # non-categorical

  # one-hot
  for n in range(N):
      t = int(X[n,D-1])
      X2[n,t+D-1] = 1

  # method 2
  # Z = np.zeros((N, 4))
  # Z[np.arange(N), X[:,D-1].astype(np.int32)] = 1
  # # assign: X2[:,-4:] = Z
  # assert(np.abs(X2[:,-4:] - Z).sum() < 1e-10)

  # assign X2 back to X, since we don't need original anymore
  X = X2

  # split train and test
  Xtrain = X[:-100]
  Ytrain = Y[:-100]
  Xtest = X[-100:]
  Ytest = Y[-100:]

  print(Xtrain[:,1])
  print(Xtrain[:,2])

  # normalize columns 1 and 2
  for i in (1, 2):
    #print(Xtrain[:,i])
    m = Xtrain[:,i].mean()     
    s = Xtrain[:,i].std()     
    Xtrain[:,i] = (Xtrain[:,i] - m) / s
    #print(Xtrain[:,i])
    Xtest[:,i] = (Xtest[:,i] - m) / s
    
  return Xtrain, Ytrain, Xtest, Ytest


def get_binary_data():
  # return only the data from the first 2 classes
  Xtrain, Ytrain, Xtest, Ytest = get_data()
  print(Xtrain[:,1]) 
  print(Xtest[:,2])
  X2train = Xtrain[Ytrain <= 1]
  Y2train = Ytrain[Ytrain <= 1]
  X2test = Xtest[Ytest <= 1]
  Y2test = Ytest[Ytest <= 1]
  return X2train, Y2train, X2test, Y2test

Xtrain, Ytrain, Xtest, Ytest = get_data()

print("******")
print(Xtrain[0,0:4])