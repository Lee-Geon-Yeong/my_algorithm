import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())    # n = 100,000 -> O(n^2) 시간초과 주의
arr = list(map(int, input().split()))

result = 0
for i in range(K):
    result += arr[i]

max_num = result
for i in range(K, N):
    result += (arr[i] - arr[i-K])   # 점화식 부분
    if max_num < result:
        max_num = result


print(max_num)