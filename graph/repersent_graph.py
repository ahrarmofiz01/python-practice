v=6#number of nodes
e=7#number of edges
edges=[(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]#edges
print(v,e,edges)
#adjancy list
adjlist=[]
for i in range(v):
    adjlist.append([])
for edge in edges:
    x=edge[0]
    y=edge[1]
    adjlist[x].append(y)
    adjlist[y].append(x)
for i in range(v):
    print(i,"->",adjlist[i])
#adjacency matrix
adjmatrix=[]
for i in range(v):
    adjmatrix.append([0]*v)
for edge in edges:
    x=edge[0]
    y=edge[1]
    adjmatrix[x][y]=1
    adjmatrix[y][x]=1
for i in adjmatrix:
    print(i)