#DFS using Recursion
graphs = {
  'a':['b','c','e'],
   'b':['d','f'],
   'c':['f','g']
}

print(graphs)
vis=[]
v = 'a'
def DFS(G, v):
    vis.append(v)
    try:
      nodes=G[v]
      for n in nodes:
        print(n)
        if n not in vis:
           DFS(G,n)
    except:
      pass
          
DFS(graphs,v)          
print(vis)          