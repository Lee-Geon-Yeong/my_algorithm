import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    goguma = list(map(int, input().split()))
    goguma_list = []
    start = 0

    for i in range(len(goguma) -1):
        if goguma[i] > goguma[i + 1]:
            goguma_list.append(goguma[start:i + 1])
            start = i + 1
            end = i + 1
    goguma_list.append(goguma[end:])

    goguma_cnt = 0

    print(goguma_list)

    flag = 0
    for i in range(len(goguma_list)):
        if len(goguma_list[i]) >= 2:
            flag = 1
            goguma_cnt += 1

    if flag == 0:
        goguma_cnt = 1


    max_num = 0
    for i in range(len(goguma_list)):
        if len(goguma_list[i]) >= max_num:
            max_num = len(goguma_list[i])




    max_goguma = 0
    for i in range(len(goguma_list)):
        if len(goguma_list[i]) == max_num:
            if sum(goguma_list[i]) >= max_goguma:
                max_goguma = sum(goguma_list[i])

    print(f"#{tc + 1} {goguma_cnt} {max_goguma}")
