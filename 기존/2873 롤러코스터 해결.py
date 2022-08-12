from sys import stdin
input=stdin.readline
R,C= map(int,input().split())

#홀수면 다 가면 됨
#짝수면 행+열이 홀수인 곳 중에서 가장 낮은 값1칸빼고 다 가면 됨


rst=''
if R%2==1:
    for i in range(R-1):
        if i%2==0:
            rst+="R"*(C-1)+"D"
        else:
            rst+="L"*(C-1)+"D"
    rst+=("R"*(C-1))

elif C%2==1:
    for i in range(C-1):
        if i%2==0:
            rst+="D"*(R-1)+"R"
        else:
            rst+="U"*(R-1)+"R"
    rst+=("D"*(R-1))




else:
    cnt=2000
    for r in range(R):
        a=list(map(int,input().split()))
        for c in range(1-r%2,C,2):
            if a[c]<cnt:
                cnt=a[c]
                nr,nc=(r,c)
                #nr,nc가면 안됨
    ROW=0
    before=0
    while ROW<R:
        if nr==ROW:
            rst+=("DRUR"*((nc-1)//2)+"DR")#R이 (nc-1)//2 +1번 R은 총 C-1번
            count=(nc//2*2+1)
            while count<C-1:
                rst+="RURD"
                count+=2
            before=1
        elif nr==ROW+1:
            rst+=("DRUR"*((nc)//2)+"RD")#R이 (nc-1)//2 +1번 R은 총 C-1번
            count=(nc//2*2+1)
            while count<C-1:
                rst+="RURD"
                count+=2
            before=1
        elif before==1:
            rst+="D"+"L"*(C-1)
            rst+="D"+"R"*(C-1)
        else:
            rst+="R"*(C-1)+"D"
            rst+="L"*(C-1)+"D"
            
        ROW+=2





print(rst)
        
