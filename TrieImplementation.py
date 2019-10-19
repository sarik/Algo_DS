class Trie:
    
    def __init__(self,string):
        self.root = {}
        self.endSymbol = "*"
        self.populateTrieFromString(string)
       
    
    def populateTrieFromString(self,string):
        
        for i in range(len(string)):
            self.poulateStringStartingFromIndex(i,string)
        
    def poulateStringStartingFromIndex(self,i,string):        
        currNode = self.root
        
        for j in range(i,len(string)):
            letter = string[j]
            #if currNode[letter] == None:
            if letter not in currNode:
                currNode[letter] = {}
            
            currNode = currNode[letter]
        
        currNode[self.endSymbol] = True
        
    
    def checkIfPresent(self,input):
        print(self.root)
        
        currNode = self.root
        
        for i in range(len(input)):
            letter = input[i]
            #if currNode[letter] == None:
            if letter not in currNode:
                return False
            else:
                currNode = currNode[letter]
                
        
        print(currNode)
        
        return (self.endSymbol in currNode)
        
trie = Trie("Papina")
print(trie.checkIfPresent("pina"))
