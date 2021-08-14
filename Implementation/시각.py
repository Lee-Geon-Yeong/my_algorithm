h=int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            sentence=str(i)+str(j)+str(k)
            # print(sentence)
            if sentence.find("3")==0:
                print(sentence)
                count+=1
            # if '3' in str(i)+str(j)+str(k):
            #     count+=1
print(count)

# find 함수는 찾는 문자 있으면 0, 없으면 -1 반환