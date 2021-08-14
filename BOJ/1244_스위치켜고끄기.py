import sys
sys.stdin = open("input.txt")

N = int(input())
switch = list(map(int, input().split()))
students = int(input())
for i in range(students):
    gender, number = map(int, input().split())
    if gender == 1:
        for j in range(number - 1, len(switch), number):    # -1을 해주는 이유는 인덱스 값을 맞춰주기 위함
            if switch[j]:
                switch[j] = 0
            else:
                switch[j] = 1
    else:
        k = 0
        while True:
            if 0 <= (number - 1 - k) and (number - 1 + k) <= len(switch) and switch[number - 1 + k] == switch[number - 1 - k]: # 인덱스 범위가 0부터 len(switch) 안에 있고 앞 뒤 값이 같을 경우
                if switch[number - 1 + k]:
                    switch[number -1 + k] = switch[number -1 - k] = 0   # 1이면 0으로
                else:
                    switch[number - 1 + k] = switch[number -1 - k] = 1  # 0이면 1로
                k += 1
            else:   # 3가지 조건을 하나라도 충족시키지 못하면 break
                break

print(" ".join(map(str, (switch))))
