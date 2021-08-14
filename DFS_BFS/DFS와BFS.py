# 삼성 SW 역량테스트에서는 sys 모듈 일부 제한 있음
# DFS의 장점 : 한 경로상의 노드를 기억하기 때문에 적은 메모리 사용, 찾으려는 노드가 깊은 단계인 경우 BFS보다 빠르다
# DFS의 단점 : 해가 없는 경로를 탐색할 경우 단계가 끝날 때까지 탐색한다. DFS는 해에 도착하면 탐색을 종료하기 때문에 최단경로라는 보장이 없다
# 모든 간선의 비용이 동일할 때는 BFS 이용

from collections import deque
n, m, v= map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b]=graph[b][a]=1

def bfs(start):
    visited=[start]
    queue=deque([start])
    while queue:    # queue에 원소 없으면 Flase, 있으면 True
        n=queue.popleft()
        for c in range(len(graph[start])):
            if graph[n][c]==1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

def dfs(start, visited):
    visited+=[start]
    for c in range(len(graph[start])):
        if graph[start][c]==1 and (c not in visited):
            dfs(c, visited)
    return visited


dfs_result=dfs(v, [])
bfs_result=bfs(v)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))

# print(*dfs(v, []))
# print(*bfs(v))
