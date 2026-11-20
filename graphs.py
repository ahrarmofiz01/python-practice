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