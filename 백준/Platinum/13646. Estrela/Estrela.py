DP=[0]*(2**16)
prime=[]
for i in range(2,2**16):
    if DP[i]==0:
        prime.append(i)
        cnt=i
        while cnt<2**16:
            DP[cnt]=1
            cnt+=i


while True:
    try:
        N=int(input())#점 개수

        rst=N
        for i in prime:
            if i>N:
                break
            if N%i==0:
        
                rst=(rst*(i-1))//i
                while N%i==0:
                    N//=i
        if N>1:
            rst=(rst*(N-1))//N
        print(rst//2)
    except:
        break
        
