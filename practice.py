import sys
sys.stdin=open('input.txt')

num = input()

for i in range(0, len(num)-7+1, 7):
    bin = num[i:i+7] # ex) 000000, 1111000

    total = 0

    for j in range(len(bin)-1, -1, -1): # 6,5,4,3,2,1,0
        if bin[j] == '1':
            total += 2 ** (len(bin) -1 -j) # 2**0, 2**1

    print(total, end=' ')