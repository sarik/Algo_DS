class Solution:
    def giveMinPath(self,grid):
        length = len(grid)
        breadth = len(grid[0])
        
        if length == 0:
            return 0
        
        return self.calculateMinPath(length-1,breadth-1,grid)
    
    def calculateMinPath(self,length,breadth,grid):
        if length ==0 and breadth ==0:
            return grid[0][0]
        
       # if(length<0 or breadth <0) or (length >= len(grid) or breadth >= len(grid[0])):
            #return 0
        
        if(length == 0):
            return grid[length][breadth] + self.calculateMinPath(length,breadth-1,grid)
        
        elif(breadth == 0):
            return grid[length][breadth] + self.calculateMinPath(length-1,breadth,grid)
               
        else:
            return grid[length][breadth] + min(self.calculateMinPath(length-1,breadth,grid),self.calculateMinPath(length,breadth-1,grid))
    
grid=[
[1,3,1],
[1,5,9],
[4,2,1]
]
print(Solution().giveMinPath(grid))
        