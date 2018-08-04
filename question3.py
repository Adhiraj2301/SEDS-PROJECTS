from collections import defaultdict
  
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
  
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    def getTranspose(self):
        g = Graph(self.V)
 
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
                print(j,",",i)
        return g
 
    
x=int(input("Enter no. of nodes\n"))
g = Graph(x)
y=int(input("Enter no. of edges\n"))
print("Enter edges\n")
for i in range(0,y):
    a=int(input("enter vertex 1 of edge:\n"))
    b=int(input("enter vertex 2 of edge:\n"))
    g.addEdge(a,b)
print("Edges of the transpose graph")
g.getTranspose()
