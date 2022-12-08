import json
import os
import sys

file = open(os.path.join(sys.path[0], 'graph.txt'), 'r')
graph = json.loads(file.read())
file.close()
visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Breadth-First Search traversing over the graph")
bfs(visited, graph, '5')

