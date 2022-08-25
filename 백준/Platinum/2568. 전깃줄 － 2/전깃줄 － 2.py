import sys
input=sys.stdin.readline

N=int(input())
#현재 가장 정확?
L=[list(map(int,input().split())) for i in range(N)]
L.sort(key= lambda x:x[1])
L=[i[0] for i in L]
DP=[]

for i in range(N):
    if not DP:
        DP.append([L[i]])
        
    elif L[i]>DP[-1][-1]:
        DP.append(DP[-1]+[L[i]])
    

    elif L[i]<=DP[0][-1]:
        DP[0]=[L[i]]
        
    else:
        #자기 '이상'인 가장 첫 원소
        target=L[i]
        Ri=len(DP)-1
        Le=1
        D=(Ri+Le)//2
        while True:
            if DP[D][-1]>=L[i] and DP[D-1][-1]<L[i]:
                DP[D]=DP[D-1]+[L[i]]
                break
            if DP[D][-1]<L[i]:
                Le=D+1
            else:
                Ri=D
            D=(Ri+Le)//2
    #print(DP)

print(len(L)-len(DP))
L.sort()
for i in L:
    if i not in DP[-1]:
        print(i)

