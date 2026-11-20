n=6#number of nodes

e=7 #number of edges
edges=[(0,1),(0,2),(0,4),(1,2),(1,5),(2,4),(3,4)]
print(edges)

#adjacency list
n=6#number of nodes

e=7 #number of edges
edges=[(0,1),(0,2),(0,4),(1,2),(1,5),(2,4),(3,4)]
adlist=[]
for i in range(n):
    adlist.append([])
for edge in edges:
    x=edge[0]
    y=edge[1]
    adlist[x].append(y)
    adlist[y].append(x)
for i in range(n):
    print(i, " ->" ,adlist[i])
# adjacency matrix
admatrix=[]
for i in range(n):
    list1=[-1]*n
    admatrix.append(list1.copy())
for i in range(e):
    a=edges[i][0]
    b=edges[i][1]
    admatrix[a][b]=1
    admatrix[b][a]=1
for i in admatrix:
    print(i)