import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(list(input()))

pattern = []
cnt = 0
result = 64
for i in range(N - 8 + 1): # 10 - 8 = 2 + 1 -> 0부터 2까지
    for j in range(M - 8 + 1): # 13 - 8 = 5 + 1 -> 0부터 5까지
        if chess[i][j] == 'W': # 시작점이 W일 때 짝수는 WB, 홀수는 BW
            for pt in range(4): # 정답 패턴 만듦
                pattern.append(['W', 'B'] * 4)
                pattern.append(['B', 'W'] * 4)
                
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if pattern[k - i][l - j] != chess[k][l]:
                        cnt += 1
            if result > cnt:
                result = cnt
            cnt = 0
        else: # 시작점이 B일 때 짝수는 BW, 홀수는 WB
            for pt in range(4):  # 정답 패턴 만듦
                pattern.append(['B', 'W'] * 4)
                pattern.append(['W', 'B'] * 4)
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if pattern[k - i][l - j] != chess[k][l]:
                        cnt += 1
            if result > cnt:
                result = cnt
            cnt = 0

print(result)