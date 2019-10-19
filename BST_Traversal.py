class Node:
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.left=left
        self.right = right
        
def inOrderTraversal(root):
    
    
    left = root.left
    right= root.right
    
       
    
    if left !=None:
        inOrderTraversal(left)
    print(root.value)
    if right !=None:
        inOrderTraversal(right)

def preOrderTraversal(root):
    
    
    left = root.left
    right= root.right
    
       
    print(root.value)
    if left !=None:
        preOrderTraversal(left)    
    if right !=None:
        preOrderTraversal(right)

def postOrderTraversal(root):
    
    
    left = root.left
    right= root.right
    
       
    
    if left !=None:
        postOrderTraversal(left)    
    if right !=None:
        postOrderTraversal(right)
    print(root.value)
    
    
#    if left == None and right == None:
#        print(root)
#    elif right == None:
#        inOrderTraversal(root.left)
#    elif left == None:
#        inOrderTraversal(root.right)
#    else:
#        inOrderTraversal(root.left)
        
        
        

A = Node(10)
B = Node(5)
C = Node(15)
D = Node(2)
E = Node(5)
F = Node(22)
G = Node(1)

A.left=B
A.right=C
B.left=D
B.right=E
C.right=F
D.left=G

#print(inOrderTraversal(A))
print(postOrderTraversal(A))

