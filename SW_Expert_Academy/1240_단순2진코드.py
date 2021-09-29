ENCODING = (
    '0001101', 
    '0011001', 
    '0010011', 
    '0111101', 
    '0100011', 
    '0110001', 
    '0101111', 
    '0111011', 
    '0110111', 
    '0001011'
)
 
T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    isExtracted = False
    secret_code = ""
    for _ in range(N):
        row = input()
        if not isExtracted and '1' in row:
            row = str(row.rstrip('0'))
            secret_code = row[-56:]
            isExtracted = True
 
    arr = []
    answer = 0
    for i in range(0,56,7):
        arr.append( ENCODING.index(secret_code[i:i+7]) )
        times = 1
        if (i // 7) % 2 == 0:
            times = 3
        answer += times * ENCODING.index(secret_code[i:i+7])
 
    if answer % 10 == 0:
        print(f"#{t} {sum(arr)}")
    else:
        print(f"#{t} 0")