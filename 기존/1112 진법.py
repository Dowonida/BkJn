def PPJB(A,N):#A를 N진법으로 나타냄.
            #A,N은 숫자
    RST=[]
    while A:
        RST.append(A%N)
        A//=N
    return RST#1의자리가 제일 앞에 있다.

def PMJB(A,N):
    if A==0:
        return 0
    a=PPJB(abs(A),abs(N))
    if N>0:
        rst=''
        for i in range(len(a)):
            rst+=str(a[-1-i])
        if A>0:
            return rst
        else:
            return '-'+rst

    else:
        N=abs(N)
        if A>0:
            for i in range(len(a)):
                a[i]*=(-1)**i
        else:
            for i in range(len(a)):
                a[i]*=-(-1)**i
        a+=[0,0]
        for i in range(len(a)-1):
            if a[i]<0:
                a[i]+=N
                a[i+1]+=1
            elif a[i]>=N:
                a[i]-=N
                a[i+1]-=1
        while not a[-1]:
            a.pop()
        rst=''
        for i in range(len(a)):
            rst+=str(a[-1-i])
        return rst     
print(PMJB(12345,10))
print(PMJB(8265,-10))
print(PMJB(1001,-2))
print(PMJB(-52,-2))
print(PMJB(-38,4))
print(PMJB(-123456789,-7))
print(PMJB(0,2))
