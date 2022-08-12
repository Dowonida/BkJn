import sys

N,K=map(int,sys.stdin.readline().split())
W=[]
V=[]
dic={}
for i in range(N):
    w,v=map(int,sys.stdin.readline().split())
    W.append(w)
    V.append(v)
V.append(0)
W.append(0)
que=[[]]#[] , [1,2,4] 처럼 넣은 물건 번호를 기록, 오름차순->중복연산하지않기위해
#que의 형태는 각 상황마다 { [1,2,3], [3,5,6]}같은식으로 저장됨
#따라서 [1,2,3], [3,5,6]에 대해서 가능한 케이스를 다음 큐에 저장
rst=0
while True:
    nextque=[]
    for i in que:#i의 형태는 [1,2,3]과 같이 물품 인덱스만 있음
        TW=sum([W[w] for w in i])#현재 무게 총합
        if i==[]:
            i.append(-1)
        hubo=[n for n in range(N) if W[n]<=K-TW and n>i[-1]]
        #더 넣을 수 있는 물품의 인덱스
        #0~n-1의 인덱스 중에서 무게가 여유무게보다 작아야하고
        #가장 큰 인덱스보다 더 커야함
        if hubo==[]:#더 넣을 수 있는 것이 없는 경우
            TV=sum([V[v] for v in i])
            if TV>rst:#가치가 기존보다 높은 경우
                rst=TV
        else:
            for j in hubo:
                nextque.append(i+[j])
    if nextque==[]:
        break
    que=nextque
    
print(rst)
