from queue import Queue

N, M = map(int, input().split())

# 탐색지도 생성
board = []
for i in range(N):
	board.append([])
	S = input()
	for s in S:
		board[i].append(int(s))

# 확인용 지도 생성(초기값 -1)
memo = [] 
for i in range(N) :
	memo.append([])
	for j in range(M) : 
		memo[i].append(-1)
        
# 이동가능 방향 
D = [[-1,0], [0,-1], [1,0], [0,1]]

# 이동한 칸 수 카운트 
memo[0][0] = 1

# 출발지 좌표
cur = [0, 0]

# 탐색할 다음좌표 : 큐 활용(put / get / empty)
q = Queue()
q.put(cur)

# BFS 알고리즘 실행
# 탐색할 큐 값이 없어질때까지 탐색
while not q.empty() :
    cur = q.get()

    # 이동가능한 다음 위치 탐색
    for d in D: 
        nxt = [cur[0]+d[0], cur[1]+d[1]] 
        if nxt[0] < 0  or nxt[1] < 0 or nxt[0] >= N or nxt[1] >= M : # 
            continue
        if board[nxt[0]][nxt[1]] != 1 :
            continue
        if memo[nxt[0]][nxt[1]] != -1:
            continue
        memo[nxt[0]][nxt[1]] = memo[cur[0]][cur[1]] + 1
        q.put(nxt)
        
print(memo[N-1][M-1])
