def solution(N, stages):
    #스테이지 별로 실패한 인원 넣을 리스트 생성
    data=[0 for i in range(N+2)]
    # 총인원수
    human=len(stages)
    #실패율 리스트 
    fail=[]
    #단계별로 실패한 인원 입력받기
    for i in stages:
        data[i]+=1
        
    #실패율과 스테이지 단계를 추가 
    for i in range(1,len(data)-1):
        #남은 인원이 0이면 실패율 0
        if human==0:
            failrate=0
        #fail리스트에 실패율과 스테이지 단계 추가
        else: 
            failrate=data[i]/human
        fail.append((failrate,i))
        #스테이지가 상승하면서 스테이지에 도달하지 못한 플레이어수를 줄여줌
        human-=data[i]
    #0요소는 내림차순, [1]요소는 오름차순
    fail=sorted(fail, key=lambda x: (-x[0], x[1]))
    answer = []
    for i in range(len(fail)):
        answer.append(fail[i][1])
    return answer

N=int(input())
# stages=[2,1,2,6,2,4,3,3]
stages=list(map(int,input().split()))
stages.sort()
solution(N, stages)