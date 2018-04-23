graphs = {
  'a':['b','c','e'],
   'b':['d','f'],
   'c':['f','g']
}
vis=[]

stack=[]


def DFS(G,v):
   
   v = stack.append('a')
   while len(stack) > 0:
         v = stack.pop()
         
         if v not in vis:
            try:
              vis.append(v)
              nodes = G[v]
              for n in G[v]:
                  stack.append(n)
            except:
              pass


DFS(graphs,'a')

print(vis)
      
   
  