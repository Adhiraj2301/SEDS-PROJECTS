from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
        m=s;
        visited = [False] * (len(self.graph))
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as 
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        d=dict()
        while queue:
 
            # Dequeue a vertex from 
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    d(i)=s
                    visited[i] = True
        for key in d.items():
            print("\n the shortest path to vertex",key," : \t")
            print(key,"\t");
            x=d[key]
            while(x!=m):
                print(d[key])
                x=d[d[key]]
                
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following are the shortest paths(starting from vertex 2)")
g.BFS(2)
