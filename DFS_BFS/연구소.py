#백준 14502번 연구소
from collections import deque
n,m=map(int,input().split())
graph=[]
queue=deque()
empty=[]
#그래프에 입력받기&바이러스&빈공간 위치찾기
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j]==2:
            queue.append((i,j))
        if graph[i][j]==0:
            empty.append([i,j])
            
#동,서,남,북 방향설정
dx=[0,0,1,-1]  
dy=[1,-1,0,0]

#bfs
def bfs(tmp_graph,tmp_queue):
    while tmp_queue:
        x,y=tmp_queue.popleft()
#         print(x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
#             print('nx=%d ny=%d'%(nx,ny))
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif tmp_graph[nx][ny]==1 or tmp_graph[nx][ny]==2:
                continue
            elif tmp_graph[nx][ny]==0:
                tmp_graph[nx][ny]=2
                tmp_queue.append((nx,ny))
#                 print('nx=%d ny=%d 큐추가'%(nx,ny))
#     print('graph=%s'%tmp_graph)
    result=0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j]==0:
                result+=1
#     print('result=%d'%result)
    return result

#조합
from itertools import combinations
#벽세우는 모든 경우 set
wall_set=list(map(list,combinations(empty,3)))

#경우의 수 돌기
value=[]
for set in wall_set:
    tmp_graph=[[] for _ in range(n)]
    tmp_queue=deque()
    #임시 graph 할당
    for i in range(n):
        tmp_graph[i]=graph[i][:]
        
    #벽세우기
    for x,y in set:
        tmp_graph[x][y]=1
        
    #임시 큐 할당
    for i in queue:
        tmp_queue.append(i)
#     print('tmp_graph=%s'%tmp_graph)
#     print('queue=%s'%tmp_queue)
     #value 리스트에 결과값 대입
    value.append(bfs(tmp_graph,tmp_queue))
print(max(value))