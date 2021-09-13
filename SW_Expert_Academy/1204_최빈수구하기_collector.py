import sys
from collections import Counter
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # c = Counter(arr).most_common(1)
    c = Counter(arr)
    c = sorted(c.items(), key=lambda x:x[0])
    # print(c[0][0])
    print(c[0])
