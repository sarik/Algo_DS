class Node:
    
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right
        

A = Node(22)
B = Node(15)
C = Node(30)
D = Node(13)
E = Node(17)
F = Node(12)
G = Node(11)

A.left = B
A.right=C
B.left=D
B.right=E
D.left=F
F.left=G
        
print(B == A.left)
 
#just go left if value to be searched is smaller than current nide
#similarly for right       
def searchValueInABinarySearchTree(root,val):
    if val == root.value:
        return root
    
    if val < root.value:
        return searchValueInABinarySearchTree(root.left,val)
    return searchValueInABinarySearchTree(root.right,val)


    
    
   
    
print(searchValueInABinarySearchTree(A,12).value)
    
    
    