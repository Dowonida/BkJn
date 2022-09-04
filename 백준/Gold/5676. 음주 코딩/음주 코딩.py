import sys
input=sys.stdin.readline



def pm(n):
    n=int(n)
    if n:
        n//=abs(n)
    return n

def segging(L,R,node):
    if L==R:
        seg[node]=A[L]
        return

    mid=(L+R)//2
    segging(L,mid,node*2)
    segging(mid+1,R,node*2+1)
    seg[node]=seg[node*2]*seg[node*2+1]


def edit(n,val):
    L=1
    R=N
    A[n]=pm(val)
    node=1
    while L<R:
        mid=(L+R)//2
        if L<=n<=mid:
            node*=2
            R=mid
        else:
            node=node*2+1
            L=mid+1

    seg[node]=pm(val)
    while node>1:
        node//=2
        seg[node]=seg[node*2]*seg[node*2+1]

def find(s,e,L,R,node=1):
    if e<L or s>R:
        return 1
    elif s<=L<=R<=e:
        return seg[node]
    else:
        mid=(L+R)//2
        return(find(s,e,L,mid,node*2)*find(s,e,mid+1,R,node*2+1))
        

while True:
    try:
        seg={}
        N, M= map(int,input().split())
        RST=''

        A=[0]+list(map(pm,input().split()))
        segging(1,N,1)

        for i in range(M):
            a,b,c= input().strip().split()
            if a=="C":
                edit(int(b),c)
            else:
                rst=find(int(b),int(c),1,N,1)
                
                if rst>0:
                    RST+='+'
                elif rst<0:
                    RST+='-'
                else:
                    RST+='0'
        print(RST)

    except:
        break
