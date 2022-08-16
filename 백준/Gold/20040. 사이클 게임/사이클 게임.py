import sys
input=sys.stdin.readline

def getting(a):
    if dic[a]==a:
        return a
    else:
        dic[a]=getting(dic[a])
        return dic[a]
def union(a,b):
    x,y=getting(a),getting(b)
    if x<y:
        dic[y]=x
    else:
        dic[x]=y
n, m = map(int,input().split())
dic={i : i for i in range(n)}

for i in range(1,m+1):
    a,b=map(int,input().split())
    if getting(a)!=getting(b):
        union(a,b)
    else:
        print(i)
        break
else:
    print(0)
    
