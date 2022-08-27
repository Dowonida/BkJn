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

    

segment={}

N, M = map(int,input().split())
List = [0]+list(map(int,input().split()))

segging(1,N,1)

for i in range(M):
    s, e = map(int,input().split())
    print(find(s,e,1,N,1))
