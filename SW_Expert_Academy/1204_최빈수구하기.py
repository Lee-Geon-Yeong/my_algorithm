import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result=[0] * 1000 # 변수 count 해 줄 빈 리스트 선언


    for i in range(1000):
        result[arr[i]] += 1 # arr 배열의 각 원소에 해당하는 값의 index에 숫자 추가

    max_num = result[999] # 같은 값이 여러개면 맨 마지막 값을 출력해야하므로 max_num를 맨 마지막 값으로 초기화

    for i in range(999, -1, -1): # 거꾸로 순회
        if result[i] > max_num:
            max_num = result[i]
            index1 = i

    print("#{} {}".format(tc + 1, index1))