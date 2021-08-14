N=int(input())
data=[]
for i in range(N):
    input_data=input().split()
    data.append((input_data[0], int(input_data[1])))

data=sorted(data, key=lambda x:x[1])

for i in data:
    print(i[0], end=' ')