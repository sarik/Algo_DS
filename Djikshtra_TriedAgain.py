import sys
class Djikshtra_TriedAgain:
    def __init__(self,graph):
        self.graph = graph
        
    def min(self,dist,vis):
        min = sys.maxsize
        indexOfMin=-1
        
        for i in range(len(dist)):
            if vis[i] == False and dist[i] < min:
                min = dist[i]
                indexOfMin = i
        
        return indexOfMin
    
    def djikshtra(self,source):
        dist = [sys.maxsize] * len(self.graph)
        vis = [False] * len(self.graph)
        dist[source] =0 
        
        for i in range(len(self.graph)):
            currVertexIndex = self.min(dist,vis)
            vis[currVertexIndex] = True
            for j in range(len(self.graph)):
                #self.graph[currVertexIndex][j] > 0 means there is path from currVertexIndex to j
                if self.graph[currVertexIndex][j] > 0 and vis[j] == False and dist[j] > dist[currVertexIndex] + self.graph[currVertexIndex][j]:
                    dist[j]= dist[currVertexIndex]+ self.graph[currVertexIndex][j]
        
        print(dist)
        self.printSolution(dist)
    
    def printSolution(self,dist):
        for node in range(len(self.graph)):
            print(node, "::", dist[node] )
            
        


actualGraph = [[0, 4, -1, -1, -1, -1, -1, 8, -1], 
           [4, 0, 8, -1, -1, -1, -1, 11, -1], 
           [-1, 8, 0, 7, -1, 4, -1, -1, 2], 
           [-1, -1, 7, 0, 9, 14, -1, -1, -1], 
           [-1, -1, -1, 9, 0, 1-1, -1, -1, -1], 
           [-1, -1, 4, 14, 10, 0, 2, -1, -1], 
           [-1, -1, -1, -1, -1, 2, 0, 1, 6], 
           [8, 11, -1, -1, -1, -1, 1, 0, 7], 
           [-1, -1, 2, -1, -1, -1, 6, 7, 0] 
          ]; 


g = Djikshtra_TriedAgain(actualGraph)   
g.djikshtra(3); 
        