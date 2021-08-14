N=int(input())

word=[]
for i in range(N):
    word.append(input())

set_word=list(set(word))

set_word.sort(key=lambda x:(len(x), x))
print(set_word)