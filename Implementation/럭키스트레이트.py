N=list(input())

left=0
right=0
for i in range(len(N)//2):
    left+=int(N[i])

for i in range(len(N)//2, len(N)):
    right+=int(N[i])

if left==right:
    print("LUCKY")
else:
    print("READY")
