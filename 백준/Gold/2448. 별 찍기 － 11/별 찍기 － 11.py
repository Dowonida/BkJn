A=['  *  ',' * * ','*****']

def ne(A):
    B=A.copy()
    N=len(A[0])//2
    for i in range(len(B)):
        B[i]=(N+1)*' '+B[i]+(N+1)*' '
    for i in A:
        B.append(i+' '+i)
    return B
    
cnt=3

N=int(input())
while cnt!=N:
    A=ne(A)
    cnt*=2
for i in A:
    print(i)
