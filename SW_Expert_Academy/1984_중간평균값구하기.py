import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop(0)
    arr.pop()
    print(f"#{tc+1} {round(sum(arr)/len(arr))}")