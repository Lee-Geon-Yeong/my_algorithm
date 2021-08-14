from collections import Counter
def mean(data):
    return round(sum(data)/N)

def median(data):
    data.sort()
    if N==1:
        return data[0]
    else:
        return (data[N//2])

def counter(data):
    c=Counter(data).most_common(2)
    if N==1:
        return data[0]
    return (c[1][0] if c[0][1]==c[1][1] else c[0][0])

def min_max(data):
    return max(data)-min(data)

N=int(input())
data=[]
for i in range(N):
    data.append(int(input()))

print(mean(data))
print(median(data))
print(counter(data))
print(min_max(data))



# counter는 {[값:빈도수]}가 큰 순서대로 정리하여 딕셔너리로 반환
# most_common은 입력값 배열 개수만큼 빈도수가 큰 순서대로 튜플형식으로 묶어 리스트로 반환
# from collections import Counter
# list=[0,1,5,3,10,3,7]
# K=Counter(list).most_common(2)
# print(K)