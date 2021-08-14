# 모든 도로의 거리가 1이므로 BFS 접근
from collections import deque
N, M, K, X= map(int, input().split())
graph=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A][B]=graph[B][A]=1

def bfs(start, min, count):
    visited=[start]
    queue=deque([start])
    
    while queue:
        n=queue.popleft()
        count+=1
        for c in range(len(graph[start])):
            if graph[n][c]==1 and (c not in visited):
                visited.append(c)
                queue.append(c)
                if min[c]<count:
                    min[c]=count
    return min    
result=bfs(X, [0]*(N+1), 0)
for i in range(1, N+1):
    if result[i]==K:
        print(i)
if K not in result:
    print("-1")
# print(result)
