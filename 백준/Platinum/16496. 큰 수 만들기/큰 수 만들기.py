import sys
input=sys.stdin.readline


def f(n):
    cnt=0
    while len(n)<10:
        n+=n[cnt]
        cnt+=1
    return n

N=int(input())
L=input().split()
L.sort(key=f,reverse=True)
rst=''
for i in L:
    rst+=i
if rst[0]=='0':
    print('0')
else:
    print(rst)
