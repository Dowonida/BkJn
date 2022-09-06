import sys
input=sys.stdin.readline

def segging(L,R,node=1):
    if L==R:
        minseg[node]=List[L]
        maxseg[node]=List[L]
        return

    mid=(L+R)//2
    segging(L,mid,node*2)
    segging(mid+1,R,node*2+1)
    minseg[node]=min(minseg[node*2],minseg[node*2+1])
    maxseg[node]=max(maxseg[node*2],maxseg[node*2+1])


def find(s,e,L,R,node=1):
    if s<=L and R<=e:#안에 들어있는 경우 
        return [node]
    elif R<s or e<L:#밖인 경우
        return []
    else:
        mid=(L+R)//2
        return find(s,e,L,mid,node*2)+find(s,e,mid+1,R,node*2+1)
        



N, M= map(int,input().split())
List=[ int(input()) for i in range(N)]
#인덱스는 0부터 N-1까지 L은 0, N-1은 R

minseg={}
maxseg={}


segging(0,N-1,1)

for i in range(M):
    s, e = map(int,input().split())
    s-=1
    e-=1
    A=find(s,e,0,N-1,1)
    print( min( minseg[k] for k in A),max(maxseg[k] for k in A))
