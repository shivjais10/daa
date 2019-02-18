from collections import defaultdict
graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)


def BFS(graph,start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    while queue:
        node=queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours=graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored



test=int(raw_input())
for k in range (0,test):
    n=int(raw_input())
    for m in range(0, n):
        x = list(map(int, raw_input().strip().split()))
        addEdge(graph,x[0],x[1])
        addEdge(graph, x[1], x[0])
    print BFS(graph,x[1])
