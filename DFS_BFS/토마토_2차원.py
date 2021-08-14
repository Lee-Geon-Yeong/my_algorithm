from collections import deque
M,N=map(int,input().split())

graph=[list(map(int, input().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((i, j))


while queue:
    x, y=queue.popleft()
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue
        if graph[nx][ny]==-1:
            continue
        if graph[nx][ny]==0:
            # graph[nx][ny]=1
            graph[nx][ny]=graph[x][y]+1
            queue.append((nx,ny))

result=-2
check_graph=False

for i in graph:
    for j in i:
        if j==0:
            check_graph=True
        result=max(result, j)
if check_graph: # check_graph가 참이면 0이 존재하므로 -1출력
    print(-1)
elif result==1:
    print(0)
else:
    print(result-1)

print(graph)