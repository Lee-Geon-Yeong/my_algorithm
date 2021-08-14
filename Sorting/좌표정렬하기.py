N=int(input())
data=[list(map(int, input().split())) for _ in range(N)]
result=sorted(data, key=lambda x:(x[0],x[1]))
for i in range(N):
    print(' '.join(map(str, result[i])))

# 조인 함수는 str만 변형 가능