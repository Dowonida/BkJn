N=int(input())
L=list(map(int,input().split()))
M=[]
for i in range(N):
    #i번째 수보다 작은 애들의 인덱스 가져오기
    LL=[j for j in range(i) if L[j]<L[i]]
    #그 애들의 길이
    if LL==[]:
        a=1
    else:
        a=max([M[j] for j in LL])+1
    M.append(a)
print(max(M))