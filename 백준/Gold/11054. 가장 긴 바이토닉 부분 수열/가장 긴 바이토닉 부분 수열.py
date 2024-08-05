import sys

N=int(sys.stdin.readline())
S=list(map(int,sys.stdin.readline().split()))
K=S.copy()
K.reverse()
cnt=0
M=[]
L=[]
for i in range(N):
    a=[M[j] for j in range(i) if S[j]<S[i]]
    b=[L[j] for j in range(i) if K[j]<K[i]]
    
    if a!=[]:
        M.append(max(a)+1)
    else:
        M.append(1)
    if b!=[]:
        L.append(max(b)+1)
    else:
        L.append(1)
rst=0
for i in range(N):
    if M[i]+L[-1-i]>rst:
        rst=M[i]+L[-1-i]
print(rst-1)