INF=int(1e9)
n=int(input())
graph=list(map(int,input().split()))
plu,sub,mul,div=map(int,input().split())
min=INF
max=-INF
def dfs(sum,i):
    global plu,sub,mul,div,max,min
    if i==n:  
        if max<sum:
            max=sum
        if min>sum:
            min=sum
        return
    if plu>0:
        plu-=1
        sum=sum+graph[i]
        dfs(sum,i+1)  
        plu+=1
        sum=sum-graph[i]
    if sub>0:  
        sub-=1
        sum=sum-graph[i]
        dfs(sum,i+1)  
        sub+=1
        sum=sum+graph[i]
    if mul>0:  
        mul-=1
        sum=sum*graph[i]
        dfs(sum,i+1)  
        mul+=1
        sum=int(sum/graph[i])
    if div>0:  
        div-=1
        sum=int(sum/graph[i])
        dfs(sum,i+1)  
        div+=1
        sum=sum*graph[i]

dfs(graph[0],1)
print(max)
print(min)
