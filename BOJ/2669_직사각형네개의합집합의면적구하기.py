import sys
sys.stdin = open('input.txt')

square=[[0 for _ in range(101)] for _ in range(101)]
# 100 크기의 배열을 선언하지 않고 더 메모리를 줄이는 방법은 없을까?

# 면적을 세기 위한 변수
cnt = 0
for i in range(4):
    x1, x2, y1, y2 = map(int, input().split())
    for i in range(x1, y1):
        for j in range(x2, y2):
            square[j][i] = 1

for i in range(101):
    cnt += square[i].count(1)

print(cnt)
