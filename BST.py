class BST:
    
    def __init__(self,value):
        self.value=value
        self.left=None 
        self.right=None
    

    def insert(self,value):
        currentNode = self
        
        while True:
            if currentNode.value > value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
                
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        
        return self
           
    
    def traverseDFS(self):
        stack=[]
        stack.append(self)
        
        while(len(stack) != 0):
            
            node = stack.pop()
            print(node.value)
            
            if(node.right != None):
                stack.append(node.right)

            if(node.left != None):
                stack.append(node.left)
        
        return self
    
    def traverseBFS(self):
        stack=[]
        stack.append(self)
        
        while(len(stack) != 0):
            
            node = stack.pop()
            print(node.value)
            
            if(node.right != None):
                stack = [node.right] + stack

            if(node.left != None):
                stack = [node.left] + stack
        
        return self


    def contains(self,val):
        currentNode = self

        while True:
            if currentNode is None:
                return False
            if currentNode.value == val:
                return True
            
            else:
                if currentNode.value < val:
                    currentNode = currentNode.right                
                else:
                    currentNode = currentNode.left

         


#BST(22).insert(9).insert(27).insert(3).insert(1).insert(22).traverseDFS().traverseBFS()
BSTcurr = BST(22).insert(9).insert(27).insert(3).insert(1).insert(22)

print(BSTcurr.contains(22))
print(BSTcurr.contains(9))
print(BSTcurr.contains(27))
print(BSTcurr.contains(3))
print(BSTcurr.contains(22))
print(BSTcurr.contains(11))
print(BSTcurr.contains(3))
print(BSTcurr.contains(33))
print(BSTcurr.contains(90))
