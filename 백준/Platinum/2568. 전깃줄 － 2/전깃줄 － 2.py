import sys
input=sys.stdin.readline
#분류를 눌러본게 잘못이지.... LIS인걸 알면 쉬움..
#잘라야하는게 왼쪽의 번호가 기준이므로
#왼쪽 번호를 수열로 둔다.
#즉 정렬을 오른쪽 번호 기준으로 한다.
#다시 말해 오른쪽 1번, 2번, 3번....에 연결된 점들에 대해서 LIS를 찾자
#그 다음 최장 수열을 찾고, 거기에 없는 값들을 출력
#다만 아래의 코드는 LIS코드로써는 다소 부적합하다.
#-> 다른 플래티넘 LIS 문제에서 시간이나 메모리초과가 뜬다.

N=int(input())
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

