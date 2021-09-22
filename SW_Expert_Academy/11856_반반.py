import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    S = list(input())
    s1 = []
    for i in S:
        if i not in s1:
            s1.append(i)
    if len(s1) == 2 and S.count(S[0]) == 2 and S.count(S[1]) == 2:
        print(f"#{tc + 1} Yes")
    else:
        print(f"#{tc + 1} No")