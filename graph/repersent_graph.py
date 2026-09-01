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
from collections import deque

# BFS
q = deque()
visited = [False] * v
ans = []

q.append(0)
visited[0] = True
ans.append(0)

while len(q) > 0:
    front = q.popleft()

    for x in adjlist[front]:
        if not visited[x]:
            q.append(x)
            visited[x] = True
            ans.append(x)

print(ans)
#dfs
stack=[]
visited=[False]*v
ans=[]
stack.append(0)
visited[0] = True

while len(stack) > 0:
    front = stack.pop()
    ans.append(front)

    for x in adjlist[front]:
        if not visited[x]:
            stack.append(x)
            visited[x] = True
            

print(ans)
