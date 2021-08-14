N=int(input())
data=[list(map(int, input().split())) for _ in range(N)]
result=sorted(data, key=lambda x:(x[1],x[0]))
for i in range(N):
    print(' '.join(map(str, result[i])))