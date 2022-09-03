import sys
from heapq import heappop, heappush
input=sys.stdin.readline
#스택을 민 세그로  구현하면
#기본으로 200만이 2**16개인 세그먼트 구성
#count값도 가지고 있음

#세그1=전체 최솟값이 새로운 값보다 작으면
#해당 값 (왼쪽노드 우선 탐색해서) 교체
#캐쉬에 값+1 (자리에 들어온 사람 개수임

#최솟값보다 새로운 값이 더 작으면
#새로운 자리가 필요함
#캐쉬에 어펜드 1

#캐쉬 길이가 자리 개수
#캐쉬의 값이 해당 자리에 사람 수

#세그먼트는 미리 10만개

def segging(L,R,node):#L은 0에서 시작, R은 99999에서 시작
                    #L,M은 인덱스임 
    if L==R:
        seg[node]=List[L]
    else:
        mid=(L+R)//2
        segging(L,mid,node*2)
        segging(mid+1,R,node*2+1)
        seg[node]=min(seg[node*2],seg[node*2+1])

def edit(node,val):
    S=size+node
    seg[S]=val
    while S>1:
        S//=2
        seg[S]=min(seg[S*2],seg[S*2+1])
        
def find(s,e,node):#나보다 작은게 무조건 있는경우만 함
                    #s보다 작은 값을 찾아서 e로 바꿈 
    if node>=size:
        edit(node-size,e)
        cs[node-size]+=1
        return
    if seg[node*2]<=s:#왼쪽이 작은 경우
        find(s,e,node*2)
    else:#아니면 오른쪽이 작지 
        find(s,e,node*2+1)

N=int(input())
size=1
while size<N:#완전으로 만들기 
    size*=2 
#size가 노드 개수
#k번 노드는 seg[k+size]에 있음 

seg={i:2000000 for i in range(size*2)}
#segging(0,size-1,1)
#k번 노드는 size+k번임 즉 range(size,2*size)범위 
#seg는 종료지점을 저장하고 있다.

H=sorted([tuple(map(int,input().split())) for i in range(N)])

    
cs=[]
for s,e in H:
    if s<seg[1]:#가장 작아서 새 노드 필요
        edit(len(cs),e)
        cs.append(1)#자리 하나 추가->기본 카운트1
    else:#기존 자리로 들어가기 #나보다 작은 왼쪽 자리 찾기
        find(s,e,1) 
        

print(len(cs))
print(*cs)
