import sys
input=sys.stdin.readline

n, k = map(int,input().split())

DP=[0]*(k+1)
DP[0]=1
L=[int(input()) for i in range(n)]

for i in L: 
    for j in range(i,k+1):
        
        DP[j]+=DP[j-i]
        
        
print(DP[-1])
#DP[j]는 가치가 i인 동전을 하나도 쓰지 않고 j원을 만드는 경우의 수이고
#DP[j-i]는 이미 지나온 항목이기에 가치가 i인 동전을 0개 이상 써서 j-i원을 만드는 경우의 수이다.
#i인 동전을 0개 이상써서 j-i원을 만드는 경우의 수는 i인 동전을 1개이상써서 j원을 만드는 경우의 수와 같다.
#따라서 DP[j]+=DP[j-i]를 해주면 된다.

#1,2,5로 10원을 만드는 과정을 살펴보자
#가장 먼저 DP테이블을 10원까지 초기화 한다.
#0원을 만드는 경우의 수는 항상 1이므로 맨 앞에는 1을 넣고 나머진 0을 채운다.
#DP=[1,0,0,0,0,0,0,0,0,0,0]
#우선 1로 10원짜리 테이블을 채워보자.
#DP[1]= 0+ DP[0]이 된다.
#DP[1]은 아직 채우지 않았으므로 아무 동전 없이 1을 만드는 경우의 수이고
#DP[0]은 동전 1이 있는 상태로 처리되었으므로 1원을 0개이상 써서 0원을 만드는 경우의 수이다.
#1원을 0개이상 써서 0원을 만드는 경우의 수는 1원을 1개이상써서 1을 만드는 경우의 수와 같다.
#이 둘을 더하면 원하는 결과가 나온다.
#이렇게 DP를 채우면 [1,1,1,1,1,1,1,1,1,1,1]이 된다.
#이제 2원을 가져와보자.
#DP[3]까지채우고 DP[4]를 넣는 과정을 보자.
#DP=[1,1,2,2,1,1,1,1,1,1,1]인 상태일 것이다.
#DP[4]는 1원만 써서 4를 만드는 경우의 수이다. 즉 1,1,1,1인 하나의 경우의 수만 있다.
#여기에 이제 DP[2]를 더해주어야 한다. DP[2]는 1,2원을 써서 2원을 만드는 경우의 수이므로
#1,1과 2가 있다. 이 각각의 경우의 수에 2를 추가해주면 1,1,2와 2,2가 된다.
#이는 2를 하나이상 써서 4원을 만드는 모든 경우의 수이다.
#따라서 2를 하나도 안쓰는 경우와 한 번 이상 쓰는 경우를 더해주면 답이 된다.
