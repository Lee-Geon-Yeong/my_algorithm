N=int(input())
dist=list(map(int,input().split()))
gas_price=list(map(int, input().split()))

sum=dist[0]*gas_price[0]
price=gas_price[0]

for i in range(1, len(dist)):
    if price<=gas_price[i]:
        sum+=price*dist[i]
    else:
        price=gas_price[i]
        sum+=price*dist[i]

print(sum)