N=int(input())
P=list(map(int, input().split()))

P.sort()
sum=0
sum1=0
for i in range(N):
    sum=sum+P[i]
    sum1=sum1+sum

print(sum1)