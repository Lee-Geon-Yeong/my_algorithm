from collections import deque

dx=[-2, -1, 1, 2, 2, 1, -1, -2]
dy=[-1, -2, -2, -1, 1, 2, 2, 1]

n=int(input())

for _ in range(n):
    q=deque()
    size=int(input())
    x, y=map(int, input().split())
    lx, ly=map(int, input().split())
    q.append((x,y,0))
    visited=[[False]*size for _ in range(size)]
    visited[x][y]=True

    while q:
        nx, ny, cnt=q.popleft()

        if lx==nx and ly==ny:
            print(cnt)
            break

        for i in range(8):
            if 0<=nx+dx[i]<size and 0<=ny+dy[i]<size and not visited[nx+dx[i]][ny+dy[i]]:
                q.append((nx+dx[i], ny+dy[i], cnt+1))
                visited[nx+dx[i]][ny+dy[i]]=True


