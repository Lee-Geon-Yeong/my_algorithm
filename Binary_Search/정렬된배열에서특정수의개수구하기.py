from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
array = list(map(int, input().split()))

def count(array, x):
  a = bisect_left(array, x)
  b = bisect_right(array, x)
  return b - a

count = count(array, m)

if count == 0:
  print(-1)
else:
  print(count)
# bisect.bisect: 값이 추가될 때 리스트가 정렬된 상태를 유지할 수 있는 위치를 반환한다.
# bisect.insort: 실제로 정렬된 상태를 유지한 채 값을 추가한다.
