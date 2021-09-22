import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 0
    for i in range(1, 10):
        if N % i == 0:
            if N // i <= 9:
                cnt += 1
    if cnt > 0:
        print(f"#{tc + 1} Yes")
    else:
        print(f"#{tc + 1} No")
