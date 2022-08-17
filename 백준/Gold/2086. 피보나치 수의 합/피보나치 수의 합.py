dic={0:[1,0,0,1],1:[1,1,1,0]}
def fipow(n):#A는 그냥 1차원배열
    if n in dic:
        return dic[n]


    elif n//2 in dic:
        dic[n]=[dic[n//2][0]*dic[n//2][0]+dic[n//2][1]*dic[n//2][2],
                dic[n//2][0]*dic[n//2][1]+dic[n//2][1]*dic[n//2][3],
                dic[n//2][2]*dic[n//2][0]+dic[n//2][2]*dic[n//2][3],
                dic[n//2][2]*dic[n//2][1]+dic[n//2][3]*dic[n//2][3]]
        for i in range(4):
            dic[n][i]%=1000000000
        return dic[n]

def matp(A,B):
    a= [A[0]*B[0]+A[1]*B[2],
                A[0]*B[1]+A[1]*B[3],
                A[2]*B[0]+A[3]*B[2],
                A[2]*B[1]+A[3]*B[3]]
    for i in range(4):
        a[i]%=1000000000
    return a

def matp2(n,m):
    if n==0:
        return dic[m]
    A=dic[n]
    B=dic[m]
    a= [A[0]*B[0]+A[1]*B[2],
                A[0]*B[1]+A[1]*B[3],
                A[2]*B[0]+A[3]*B[2],
                A[2]*B[1]+A[3]*B[3]]
    for i in range(4):
        a[i]%=1000000000
    return a

m,N=map(int,input().split())
m,N=min(m,N),max(m,N)
n=1
n2=1
N+=2
m+=1

while n<=N:
    fipow(n)
    n*=2
lst=[]
cnt=1
while N:
    lst.append(N%2*cnt)
    N//=2
    cnt*=2
A=dic[lst.pop(0)]
while lst:
    A=matp(A,dic[lst.pop(0)])

    
    
while n2<=N:
    fipow(n2)
    n*=2
lst2=[]
cnt=1
while m:
    lst2.append(m%2*cnt)
    m//=2
    cnt*=2
B=dic[lst2.pop(0)]
while lst2:
    B=matp(B,dic[lst2.pop(0)])
        
    
print((A[0]-A[3]-B[0]+B[3])%1000000000)
