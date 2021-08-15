x, y = map(int, input().split())
tc = int(input())

x_arr = [0, x]
y_arr = [0, y]

for _ in range(tc):
    number, cut = map(int, input().split())
    if number:
        x_arr.append(cut)
    else:
        y_arr.append(cut)

x_arr.sort()
y_arr.sort()

# 최대 사각형 넓이 변수
max_square = 0

# 좌측 상단부터 비교
for i in range(1, len(x_arr)):  # -1번째와 비교하기 위해 기준이 1부터 시작, 0부터면 out of index 오류 뜸
    for j in range(1, len(y_arr)):
        w = x_arr[i] - x_arr[i-1]   # 0에서 4, 4에서 10 -> 2개의 split
        h = y_arr[j] - y_arr[j-1]   # 0에서 2, 2에서 3, 3에서 8 -> 3개의 split
        max_square = max(max_square, w * h)

print(max_square)