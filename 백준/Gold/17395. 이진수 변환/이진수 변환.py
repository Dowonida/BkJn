X, N = map(int,input().split())
#이진법으로 바꾼 다음에
#1의 개수를  세고
#1의 개수가 N보다 적으면 -1출력
#1의 개수가 N개이상이면
#맨 뒤의 1들을 개수에 맞춰서 자름

cnt = 1
while cnt<X:
    cnt*=2
L=[]
while cnt:
    if cnt<=X:
        X -= cnt
        L.append(X)
    cnt//=2

#print(L)

if len(L)<N:
    print(-1)
else:
    while len(L)>=N:
        L.pop()
    L.append(0)
    print(*L)
