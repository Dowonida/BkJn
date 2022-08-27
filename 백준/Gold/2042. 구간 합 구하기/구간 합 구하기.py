import sys
input = sys.stdin.readline

def segging(Left, Right, node):
    if Left==Right:
        segment[node]=List[Left]
        return

    mid=(Left+Right)//2
    segging(Left,mid,node*2)
    segging(mid+1,Right,node*2+1)
    segment[node]=segment[node*2]+segment[node*2+1]
    

def find(s,e,Left,Right,node=1,answer=0):
    if s<=Left and Right<=e:
        return segment[node] 
    elif s>Right or e<Left:
        return 0
    else:
        mid=(Left+Right)//2
        answer+=find(s,e,Left,mid,node*2)+find(s,e,mid+1,Right,node*2+1)
    return answer

def segedit(target,value,Left,Right,node=1):
    if Left==Right==target:
        List[target]=value
        segment[node]=value
        return
        
    if Left<=target<=Right:
        mid=(Left+Right)//2
        diff=value-List[target]
        segment[node]+=diff
        segedit(target,value,Left,mid,node*2)
        segedit(target,value,mid+1,Right,node*2+1)
    else:
        return
        

segment={}

N, M, K = map(int,input().split())
List = [0]+list(int(input()) for i in range(N))

segging(1,N,1)

for i in range(M+K):
    a, b, c = map(int,input().split())
    if a==1:
        segedit(b,c,1,N)
    else:
        print(find(b,c,1,N))
