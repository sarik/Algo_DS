import numpy as np
import pandas as pd

line = np.linspace(-2,2,3)
print(line)
xx,yy=np.meshgrid(line,line)
print(xx)
print(yy)
print(np.vstack((xx,yy)).T)
print(yy.shape)
print(yy.flatten())
print(yy.flatten().shape)

i=2
print(i * False)


print(np.random.rand(3,2))
print(np.random.randn(3,2))

#return random floats in the half-open interval [0.0, 1.0).
#to return floats in range(a-b) multiply by (b-a) and add a
print((2 - (-2)) *np.random.random((3,2)) + (-2))
print(np.random.random((3,2)) * 4-2)