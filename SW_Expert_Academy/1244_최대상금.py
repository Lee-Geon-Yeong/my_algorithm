import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(4):
    reward, cnt = map(int, input().split())
    reward = list(map(int, (str(reward))))

    start = -1

    for i in range(cnt): # 1
        max_num, idx = reward[-1], len(reward) - 1 # max_num = 3, idx = 2
        start += 1 # 0

        for j in range(len(reward) - 2, start - 1, -1): # j = 1, 0
            print(j, max_num)
            if reward[j] > max_num: # reward[j] = 2, max_num = 3
                max_num, idx = reward[j], j # max_num = 3, idx = 1
                
        reward[start], reward[idx] = reward[idx], reward[start] 

    print(reward)