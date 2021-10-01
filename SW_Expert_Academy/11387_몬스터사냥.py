import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(T):
    D, L, N = map(int, input().split())
    result = 0

    for i in range(N):
        result += D*(1 + i * L / 100)
    print(f"#{tc+1} {int(result)}")