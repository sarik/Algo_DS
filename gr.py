import numpy as np
from matplotlib import pyplot as plt

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))

T = np.linspace(-5,5,10)
print(T)

Y = sigmoid(T)
print(Y)

plt.plot(T,sigmoid(T))
plt.plot(T,sigmoid_p(T))