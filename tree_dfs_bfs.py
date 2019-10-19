import collections as ds
q=ds.deque([1,2,3,4,5])
q.append(22)
q.append(33)
q.popleft()
print(q)



a =[1,2,3]
b=[4,5,6]
stack = b + a
print(stack)



class Node:
    def __init__(self,value,children=None):
        self.value=value
        self.children=children
        
def dfs(node):
    stack=[]
    curr=node
    stack.append(curr)
    while(len(stack) > 0):  
        popped =stack.pop()
        print(popped.value)
        if popped.children !=None:
            stack += reversed(popped.children)
            #for child in popped.children:
                #stack.append(child)
                
def bfs(node):
    stack=[]
    curr=node
    stack.append(curr)
    while(len(stack) > 0):  
        popped =stack.pop()
        print(popped.value)
        if popped.children !=None:
            stack = popped.children + stack
            #print(stack)
            #for child in popped.children:
                #stack.append(child)
        
a=Node('A')
b=Node('B')
c=Node('C')
d=Node('D')
e=Node('E')
f=Node('F')
g=Node('G')
h=Node('H')
i=Node('I')

a.children=[b,c,d]
b.children=[e,f]
c.children=[g,h]
e.children=[i]

dfs(a)
print("******888")
bfs(a)
            
        
    