import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

def get(a):
    if dic[a]==a:
        return a
    else:
        dic[a]=get(dic[a])
        return dic[a]

def union(a):
    x=get(a)
    dic[x]-=1


N=int(input())
K=int(input())
#L= [ int(input()) for i in range(N)]

dic={i:i for i in range(N+1)}

for i in range(1,1+K):
    a=int(input())
    if get(a)==0:
        print(i-1)
        break
    union(a)
else:
    print(K)
    #print(i,dic)
