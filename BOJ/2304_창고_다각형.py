import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

max_num = 0
for i in range(N):
    if max_num < arr[i][1]:
        max_num = arr[i][1]
        max_idx = i

mid = max_idx   # 3

cnt = arr[max_idx][1]

for i in range(mid):
    if arr[i][1] <= arr[i+1][1]:
        cnt += (arr[i+1][0]-arr[i][0]) * arr[i][1]
    else:
        arr[i+1][1] = arr[i][1]
        cnt += (arr[i+1][0]-arr[i][0]) * arr[i][1]

for i in range(N-1, mid, -1):
    if arr[i][1] <= arr[i-1][1]:
        cnt += (arr[i][0]-arr[i-1][0]) * arr[i][1]
    else:
        arr[i-1][1] = arr[i][1]
        cnt += (arr[i][0]-arr[i-1][0]) * arr[i][1]

print(cnt)
