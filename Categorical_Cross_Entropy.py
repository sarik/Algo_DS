import numpy as np

a=np.array([1,2,3,4,5,6])
b=np.array([0,1,1,2,0,0])
print(a[b>0])

#regualr categorical cross entropy .Uses N*K hot encoding to represent
a = np.array([[1,0,0],[0,1,0],[0,0,1],[1,0,0]])


b = np.array([[0.1,0.2,0.3],[0.1,0.2,0.3],[0.1,0.2,0.3],[0.1,0.2,0.3]])

#print(a)

#b[[allRowIndex],[allColumnindex]]
#print(b[[0,1,2,2],[1,2,2,1]])


print(b[np.arange(4),np.argmax(a,axis=1)])


#sparse categorical cross entropy .Uses vector of size N (actual targets)
#so representing a now as
a = np.array([0,1,2,0])
print(b[np.arange(4),a])