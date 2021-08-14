# 끝나는 시간이 제일 빠른 것들 중에서 겹치지 않은 수업을 고르면 된다
# 끝나는 시간이 제일 빠른 순으로 정렬
n=int(input())
time=[list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x:(x[1], x[0]))
endtime=time[0][1]
count=1
for i in range(1, n):
    if time[i][0]>=endtime:
        endtime=time[i][1]
        count+=1
print(count)