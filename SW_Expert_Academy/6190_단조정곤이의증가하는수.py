import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = -1

    for i in range(N-1):
        for j in range(i+1, N):
            danjo = arr[i] * arr[j]
            danjo_list = list(map(int, str(danjo)))
            print(danjo_list)

            flag = 0
            temp = 0
            for k in danjo_list:
                if temp <= k:
                    temp = k
                else:
                    flag = 1
                    break

            if flag == 0:
                if result <= danjo:
                    result = danjo

    print(f"#{tc+1} {result}")