N=int(input())
data=[list(input().split()) for _ in range(N)]
data.sort(key=lambda x:(int(x[0])))

print(data)
# for i in data:
#     print(data[0], data[1])