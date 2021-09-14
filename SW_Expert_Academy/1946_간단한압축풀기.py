import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = ''

    for _ in range(N):
        C, K = input().split()
        result += C * int(K)
    # print(result) AAAAAAAAAABBBBBBBCCCCC
    print("#{}".format(tc))

    cnt = 0 # 출력할 행의 개수
    for i in range(len(result)//10 + 1): # 0, 1, 2
        print(result[cnt:cnt + 10])
        cnt += 10
