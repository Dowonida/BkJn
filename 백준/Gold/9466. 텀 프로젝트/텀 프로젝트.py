import sys
input=sys.stdin.readline

T=int(input())
#기본적으론 쭉 늘어놓다가 싸이클생기면 싸이클 앞의 가지를 잘라냄
#이럴 경우, 싸이클이 먼저나와서 가지가 나중에 생기면
#가지의 도착지점이 없어 인덱스에러 가능성 생김
#8자 같은건 안생김 왜냐면 8자가 되려면 가운데가 2명을 골라야함
#자기자신을 고르면? 
for test_case in range(T):
    N=int(input())
    L=[0]+list(map(int,input().split()))#인덱스 맞추기용
    survived={i for i in range(1,N+1)}
    rst=0
    while survived:
        
        a=survived.pop()
        team=[a]
        while True:
            a=team[-1]
            if a==L[a]:
                rst+=len(team)-1
                break
            if L[a] in survived:#살아있으면 일단 추가 
                survived.remove(L[a])
                team.append(L[a])
                    
            else: #이번에 죽었으면 싸이클돌았으니 앞에놈 다 잡기 
                if L[a] in team:#팀에 있으면 while탈출하고 rst계산
                    rst+=team.index(L[a])
                    break
                else:#팀에 없으면 그대로 추가 
                    rst+=len(team)
                    break
    print(rst)
