N, K=map(int, input().split())
coin_types=[0 for _ in range(N)]
for i in range(N):
    coin_types[i]=int(input())

coin_types.sort(reverse=True)
count=0
for i in range(N):
    if K>coin_types[i]:
        count=count+K//coin_types[i]
        K=K%coin_types[i]
print(count)