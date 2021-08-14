import sys
sys.setrecursionlimit(10**6)

countList = []
T = int(sys.stdin.readline())

def dfs(mat, y, x):
    mat[y][x] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if mat[ny][nx] == 1:
                dfs(mat, ny, nx)


for _ in range(T):

    # M: x, N: y
    M, N, K = map(int, sys.stdin.readline().split())

    inputList = [list(map(int, sys.stdin.readline().split())) for _ in range(0, K)]

    mat = [ [0]*M for _ in range(N)]

    for x, y in inputList:
        mat[y][x] = 1

    cnt = 0
    for y in range(0, N):
        for x in range(0, M):
            if mat[y][x] == 1:
                dfs(mat, y, x)
                cnt += 1

    countList.append(cnt)

for i in countList:
    print(i)

