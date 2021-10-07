import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    result = 0
    for i in range(K):
        result += arr[i]
    print(f"#{tc + 1} {result}")