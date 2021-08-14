N, K = map(int, input().split())
data = []
index = []
for i in range(N):
    data.append(list(map(int, input().split())))

S, X, Y= map(int, input().split())

for i in range(N):
    for j in range(N):
        for L in range(1, K+1):
            if data[i][j]==L:
                index.append((i, j))

print(index)

 