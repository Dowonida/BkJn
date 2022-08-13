import sys
input=sys.stdin.readline

N,Q = map(int, input().split())
dic={}

for i in range(N):
    dic[i+1]=list(map(int,input().split()))+[i+1]#4번째 값을 번호로 
L=list(dic.values())
L.sort()

S=[[L[0][0],L[0][1]]]
L[0][2]=1

for i in range(1,len(L)):
    if L[i][0]<=S[-1][1]:
        S[-1][1]=max(S[-1][1],L[i][1])
    else:
        S.append([L[i][0],L[i][1]])
    L[i][2]=len(S)



for i in range(Q):
    a,b=map(int,input().split())
    if dic[a][2]==dic[b][2]:
        print(1)
    else:
        print(0)
