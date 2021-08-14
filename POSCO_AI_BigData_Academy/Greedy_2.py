#input data
# 5 8 3
# 2 4 5 4 6
# N, M, K=input().split()
# print(type(N))
# print(N, M, K)

N, M, K=map(int, input().split())
data=list(map(int, input().split()))

data.sort(reverse=True)
first=data[0]
second=data[1]
result=0
while True:
    for i in range(K):
        if M==0:
            break
        result+=first
        M-=1
    if M==0:
        break
    result+=second
    M-=1

print(result)
