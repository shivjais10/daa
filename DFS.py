from collections import defaultdict
graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)

def DFS(graph,start):
    global vistedd
    stack=[start]
    visited=[]
    while stack:
        node=stack.pop(-1)

        if node not in visited:
            visited.append(node)
            visitedd.append(node)
            for neighbour in graph[node]:
                stack.append(neighbour)
    return visited






n=int(raw_input())
for m in range(0, n):
        x = list(map(int, raw_input().strip().split()))
        addEdge(graph,x[0],x[1])
        addEdge(graph, x[1], x[0])
vert=int(raw_input())
c=[]
visitedd=[]
for i in range(0,vert):
    if i not in visitedd:
        c.append(DFS(graph,i))

print c
