import sys
sys.stdin = open('input.txt')
def node_hap(node):
    if N - M < node <= N:
        return tree[node]
    elif node > N:
        return 0
    else:
        left = node_hap(node * 2)
        right = node_hap(node * 2 + 1)
        tree[node] = left + right
        return tree[node]


T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node_num, value = map(int, input().split())
        tree[node_num] = value
    node_hap(1)
    # print(f'#{tc + 1} {tree[L]}')
    print(tree)