import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    rock = []
    for _ in range(N):
        rock.append(input())

    answer = 'NO'

    # 가로 부분
    for i in range(N):
        garo = rock[i].count('o')
        if garo == 5:
            answer = 'YES'

    # 세로 부분
    reverse = []
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += rock[j][i]
        reverse.append(temp)
    for i in range(N):
        sero = reverse[i].count('o')
        if sero == 5:
            answer = 'YES'

    # 대각선 부분
    # 좌상, 좌하, 우상, 우하
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    for i in range(N):
        for j in range(N):
            if rock[i][j] == 'o':
                for k in range(4):
                    cross = 1
                    ni = i
                    nj = j
                    for _ in range(5):
                        nx = ni + dx[k]
                        ny = nj + dy[k]
                        if (0 <= nx < N) and (0 <= ny < N):
                            if rock[nx][ny] == 'o':
                                cross += 1
                                ni = nx
                                nj = ny
                    if cross == 5:
                        answer = 'YES'

    print(f"#{tc+1} {answer}")