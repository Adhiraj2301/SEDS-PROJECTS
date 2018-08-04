from collections import defaultdict
  
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
  
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    
    def DFSUtil(self,v,visited):
        
        visited[v]= True
        print(v),
        
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
 
 
    def fillOrder(self,v,visited, stack):
        
        visited[v]= True
        
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
     
 
    def getTranspose(self):
        g = Graph(self.V)
 
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
 
    def printSCCs(self):
         
        stack = []
        
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
 
        gr = self.getTranspose()
         
        visited =[False]*(self.V)
 
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                print("")
x=int(input("Enter no. of nodes\n"))
g = Graph(x)
y=int(input("Enter no. of edges\n"))
print("Enter edges\n")
for i in range(0,y):
    a=int(input("enter vertex 1 of edge:\n"))
    b=int(input("enter vertex 2 of edge:\n"))
    g.addEdge(a,b)
print("Following are strongly connected components in given graph")
g.printSCCs()
