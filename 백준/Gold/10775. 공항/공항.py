import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

def get(a):
    if dic[a]==a:
        return a
    else:
        dic[a]=get(dic[a])
        return dic[a]
N=int(input())
dic={i : i for i in range(N+1)}

M=int(input())
for i in range(M):
    a=int(input())
    if dic[get(a)]:
        dic[get(a)]=get(a)-1
    else:
        print(i)
        break
else:
    print(N)
