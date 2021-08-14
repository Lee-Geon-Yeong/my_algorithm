# DFS로 푸는 게 효과적
n = int(input())
m = int(input())

graph=[[0]*(n+1) for _ in range(n+1)]
visited_list=[0]*(n+1)
for i in range(m):
    a, b=map(int, input().split())
    graph[a][b]=graph[b][a]=1

infected_comp=[]

def dfs(v):
    visited_list[v]=1
    infected_comp.append(1)
    for i in range(n+1):
        if visited_list[i]==0 and graph[v][i]==1:
            dfs(i)

dfs(1)
print(len(infected_comp)-1)

