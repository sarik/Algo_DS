import sys 

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
        
    def getMinimumVertex(self,visited,dis):
        min = sys.maxsize
        ver = 0
        
        for i in range(len(visited)):
            if not visited[i] and dis[i] < min :
                min = dis[i]
                ver = i
                
        
        return ver
  
    def dijkstra(self,src):
        
        visited = [False for column in range(self.V)]
        dis = [sys.maxsize for column in range(self.V)]
        dis[src] = 0
        
        for i in range(self.V):
            minVertex = self.getMinimumVertex(visited,dis)
            visited[minVertex]= True
            
            for j in range(self.V):
                if not visited[j] and self.graph[minVertex][j] > 0:
                    if dis[j] > dis[minVertex] + self.graph[minVertex][j]:
                        dis[j] = dis[minVertex] + self.graph[minVertex][j]
        
        print(dis)
            
  
# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 
  
g.dijkstra(3); 
  
# This code is contributed by Divyanshu Mehta 