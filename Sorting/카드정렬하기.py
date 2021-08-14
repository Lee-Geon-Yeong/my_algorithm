import sys
import heapq

n = int(sys.stdin.readline())
m = []
for _ in range(n):
    heapq.heappush(m, int(sys.stdin.readline()))    # heapq에 값 저장

if len(m) == 1:
    print(0)
else:
    result = 0
    while len(m) > 1:
        temp1 = heapq.heappop(m)      # 최솟값 1개 뽑기
        temp2 = heapq.heappop(m)      # ''
        result += temp1 + temp2     # 최소값 두개 합산
        heapq.heappush(m, temp1 + temp2)     # 더한값을 heapq에 넣어줌
    print(result)

# heappush(heap, item) : O(logN) : heap에 item을 넣은 후 배열 수정
# heappop(heap) : O(logN) : heap에서 최소값 출력 후 배열 수정
# heappushpop(heap,item) : O(logN) : heap에 item을 넣고, 최소값 출력
# heapify(x) : O(NlogN) : list x를 heap구조로 변환
