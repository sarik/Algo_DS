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

def findLargestSumInBinaryTree(root):   
    answer =0        
    
    leftSubtreeRoot = root.left
    rightSubtreeRoot = root.right
    
    if leftSubtreeRoot == None and rightSubtreeRoot == None:
        return root.value
    elif leftSubtreeRoot == None:
        answer = root.value + findLargestSumInBinaryTree(rightSubtreeRoot)
    elif rightSubtreeRoot == None:
        answer = root.value + findLargestSumInBinaryTree(leftSubtreeRoot)
    else:
        answer  = max(root.value + findLargestSumInBinaryTree(leftSubtreeRoot) , root.value + findLargestSumInBinaryTree(rightSubtreeRoot))
       
    return answer

print(findLargestSumInBinaryTree(A))


