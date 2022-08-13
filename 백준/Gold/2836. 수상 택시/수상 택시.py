import sys
input=sys.stdin.readline
#앞에서 타서 뒤에서 내리는 정주행은 계산할 필요 없음
#전체길이로 퉁치면 됨
#뒤에서 타서 앞에서 내리는 역주행의 경우 계산해야함
#선분을 그어서 겹치는 선분을 하나로만들고
#해당 선분 길이를 추가로 왕복해야하므로 왕복길이*2
#따라서 총 이동거리는 전체길이+왕복선길이 두배

N, M=map(int,input().split())
L=[]
for i in range(N):
    a,b=map(int,input().split())
    if a>b:
        L.append((b,a))
L.sort()
if L:
    S=[[L[0][0],L[0][1]]]
    for i in range(1,len(L)):
        if L[i][0]<=S[-1][1]:#출발점이 도착점 이전에 있으면
            S[-1][1]=max(S[-1][1],L[i][1])#도착점은 더 뒤에 있는걸로
        else:
            M+=2*(S[-1][1]-S[-1][0]) #해당 구간 왕복길이 더해줌
            S.append([L[i][0],L[i][1]])
            
    M+=2*(S[-1][1]-S[-1][0])#마지막 구간도 계산 해줌 

print(M)
