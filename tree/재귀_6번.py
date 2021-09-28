import sys
sys.stdin=open('input.txt')

def preorder(graph, node, visited):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            preorder(graph, i, visited)

V, Node = map(int, input().split())
visited=[0 for _ in range(1000)]
graph = [

]
preorder(graph, 1, visited)