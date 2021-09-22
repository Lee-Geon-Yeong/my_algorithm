import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    direction = input()
    node = a = b = 1
    for i in direction:
        if i == 'L':
            node = a / (a + b)
            b = (a + b)
        else:
            node = (a + b) / b
            a = (a + b)
    print(f"#{tc + 1} {a} {b}")