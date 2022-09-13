def lcm(a,b):
    x,y=a,b
    while x:
        x,y = y%x,x
    return a*b//y

N= int(input())

dic={}
want= list(map(int,input().split()))
L={}
M = list(map(int,input().split()))

Max=1
for i in range(N):
    if i not in dic:
        cnt=[i]
        j=M[i]
        while j!=i:
            cnt.append(j)
            j=M[j]
        cnt2=list(map(lambda x:x%3, cnt))
        for j in range(len(cnt)):
            dic[cnt[j]]=cnt2[j:]+cnt2[:j]
            L[cnt[j]]=len(cnt)
        Max=lcm(Max,len(cnt))
        
for i in range(Max):
    for j in dic:
        if want[j]!=dic[j][i%L[j]]:
            break
    else:
        print(i)
        break
else:
    print(-1)
        
