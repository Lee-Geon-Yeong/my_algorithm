N=int(input())
x, y=1, 1
plans=input().split()

dx=[0, 1, -1, 1]
dy=[-1, 1, 0, 0]
move_types=['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    x, y=nx, ny

print(x, y)

# continue일 때 아래로 내려오지 않고 다시 for문 위로 올라감
# break일 때 for문 탈출