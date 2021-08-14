N=int(input())

data=[list(input().split()) for _ in range(N)]

data=sorted(data, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(data[i][0])