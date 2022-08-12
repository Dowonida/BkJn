#30840kb, 68ms
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
        a[i]%=1000000007
    return a

N,M=map(int,input().split())
n=1
R=N
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

fn=A[1]
fnp=A[3]
rst=0

while R<M+1:
    rst+=fn
    x=fn+fnp
    fnp=fn%1000000000
    fn=x%1000000000
    R+=1
    rst%=1000000000
print(rst)
