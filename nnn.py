import numpy as np

def nn(a1,a2,w1,w2,b):
    return sigmoid(a1*w1 + a2*w2 + b);

def sigmoid(x):
    return 1/(1+np.exp(-x))

w1 = np.random.randn()

w2 = np.random.randn()

b = np.random.randn()

print(nn(1,2,w1,w2,b))

#graph (b-4) ** 2
def slope(b):
    return 2*(b-4)

b = 8

for i in range(16):
    print("slope at ")
    print(b)
    print(slope(b))
    b = b - (slope(b)* 0.1)
    #print(b)




