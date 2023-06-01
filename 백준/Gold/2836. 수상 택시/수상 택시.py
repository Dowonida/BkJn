import sys
input = sys.stdin.readline

'''
역행을 유니온할까


'''
L = []
N, M = map(int,input().split())

for _ in range(N):
    a,b = map(int,input().split())
    if a>b:
        L.append((b,a))
L.sort()
L.append((M+1,M+1))
rst = M
s=e=0
for a,b in L:
    if a<=e:
        e=max(b,e)
    else:
        rst += 2*(e-s)
        s=a
        e=b
print(rst)
    
