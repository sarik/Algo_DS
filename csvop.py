import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def getData(balance_ones=True):
    # images are 48x48 = 2304 size vectors
    Y = []
    X = []
    first = True
    count=0
    for line in open('fer2013.csv'): 
        #print(line)
        #taking first 20 rows
        if count>20:
            break
        count += 1      
        if first:
            #print(line)#emotion,pixels,Usage
            first = False
        else:
            row = line.split(',')
            Y.append(int(row[0]))
            X.append([int(p) for p in row[1].split()])

    X, Y = np.array(X) / 255.0, np.array(Y) 
    print(X.shape,Y.shape) #(20, 2304) (20,)

    if balance_ones:
        # balance the 1 class
        X0, Y0 = X[Y!=1, :], Y[Y!=1]
        X1 = X[Y==1, :]
        X1 = np.repeat(X1, 9, axis=0)
        X = np.vstack([X0, X1])
        Y = np.concatenate((Y0, [1]*len(X1)))  

    #print(X,"inside")
    return X ,Y

X ,Y= getData(balance_ones=False)
#print(X[-1:].shape)

label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
while True:
        for i in range(7):
            x, y = X[Y==i], Y[Y==i]
            N = len(y)
            j = np.random.choice(N)
            plt.imshow(x[j].reshape(48, 48), cmap='gray')
            plt.title(label_map[y[j]])
            plt.show()
        prompt = input('Quit? Enter Y:\n')
        if prompt == 'Y':
            break

