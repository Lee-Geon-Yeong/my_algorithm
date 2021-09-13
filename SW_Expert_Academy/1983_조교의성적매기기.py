import sys
import numpy as np
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1):
    grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    N, K = map(int, input().split())
    score = []
    for i in range(N):
        mid, final, homework = map(int, input().split())
        score.append(mid * 0.35 + final * 0.45 + homework * 0.2)

    score_sorted = np.sort(score) # score 정렬
    score_sorted_index = np.argsort(score) # score의 정렬된 index 반환

    # print(score)
    # print(score_sorted)
    # print(score_sorted_index)

    same = N / 10
    cnt = 0
    for i in range(0, N):
        for j in range(same):
