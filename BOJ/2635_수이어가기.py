N = int(input())

arr = [[N] for _ in range(N // 2)] # 모든 배열에는 N이 첫번째 원소로 고정
max_len = 0
max_len_idx = 0
for i in range(N // 2, N):  # i = 5, 6, 7.... 이지만 배열은 0부터 시작하므로
    arr_idx = i - (N // 2)  # 저장할 배열의 idx를 다른 변수에 만들어줌
    arr[arr_idx].append(i)  # 두 번째 원소는 무조건 N에서 i를 뺀 값이 되므로 2번째 값은 i로 지정
    while True:
        if arr[arr_idx][len(arr[arr_idx])-2] < arr[arr_idx][len(arr[arr_idx])-1]: # 배열의 마지막 원소가 그 전의 원소보다 크면 break
            break
        next = arr[arr_idx][len(arr[arr_idx])-2] - arr[arr_idx][len(arr[arr_idx])-1] # 세 번째 값부터는 자기에서 -2번째, -1번째를 빼 준 결과값 저장
        arr[arr_idx].append(next)

    if max_len < len(arr[arr_idx]): # 최대 길이의 배열과 인덱스 저장
        max_len = len(arr[arr_idx])
        max_len_idx = arr_idx

print(" ".join(map(str, (arr[max_len_idx]))))