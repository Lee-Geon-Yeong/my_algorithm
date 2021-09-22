import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    P = input()
    Q = input()

    if P + 'a' == Q:
        print(f"#{tc+1} N")
    else:
        print(f"#{tc + 1} Y")