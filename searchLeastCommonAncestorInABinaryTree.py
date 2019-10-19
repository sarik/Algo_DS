class Node:
    
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right
        

A = Node(22)
B = Node(12)
C = Node(2)
D = Node(11)
E = Node(5)
F = Node(6)
G = Node(3)

A.left = B
A.right=C
B.left=D
B.right=E
D.left=F
F.left=G
        
print(B == A.left)
        
def searchLeastCommonAncestorInABinaryTree(root,node1,node2):
    if root == None:
        return None
    
    if node1 == root or node2 == root:
        return root
    
    if node1 == None and node2 == None:
        return None
    
    
    print(root.value)
    left =  searchLeastCommonAncestorInABinaryTree(root.left,node1,node2)
    right = searchLeastCommonAncestorInABinaryTree(root.right,node1,node2)
    
    if left != None and right != None:
        return root
    
    if left == None and right == None:
        return None
    
    return right if left == None else left
    
print(searchLeastCommonAncestorInABinaryTree(A,D,E).value)
    
    
    