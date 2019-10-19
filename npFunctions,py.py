import numpy as np
from sklearn.utils import shuffle

def softmax(x):
    xExp=np.exp(x)
    print(x.sum(axis=1))
    xE= xExp/xExp.sum(axis=1,keepdims=True)
    return xE

#print(softmax(np.array([[2,2,2],[4,5,6]])))
a=np.array([[1,2,3],[4,5,6]])
print(a+[1,-1,1])

print(a.sum(axis=0))
print(np.sum(a,axis=0))


a=np.array([1,2,3])
print(a*(a>1))
b=np.array([4,5,6])
print(a*(b>5))
print(a.dot(b))
c,d = shuffle(a,b)
print(c)
print(d)
print(np.outer(a,b))

k=np.zeros((len(a),max(a)+1))


for i in range(len(a)):
    #print(a[i])
    k[i][a[i]]=1
    
print(k)
    

a = np.array([[1,2,3,4,5,6,7,8,9],[1,1,1,2,2,2,3,3,3]])
b=a.reshape(2,3,3)
print(b)

c=[]
for i in range(len(b)):
    c.append(np.sum(b[i]))

print(c)


X=np.array([[1,2],[3,4]])
XRepeated=np.repeat(X,3,axis=1)
print(XRepeated)
print(XRepeated.shape,X.shape)
    

X=np.random.rand(10000,10000)

m = X.mean()
s = X.std()

X=X-np.mean(X)/np.std(X)
#X = (X - m) /s


print(X[:10])

arr=[2,4,6,10]
print(arr[1:])


data = [[3,"23 34 43 56 78",1],[3,"23 35 43 56 78",2],[3,"23 36 43 56 78",3]]

p=[]

Y = []
for i in range(len(data)):
    Y.append(data[i][len(data[i])-1])
    pix=[int(pi) for pi in data[i][len(data[i])-2].split()]
    #print(pix)
    p.append(pix)
    
    
    

print(p)
