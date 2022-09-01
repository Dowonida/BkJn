#N까지 1을 약수로 갖는 친구 수=N-1
#N까지 2를 실질적 약수로 갖는 친구수= N//2-1...
N=int(input())
rst=0
for i in range(2,N):
    rst+=i*(N//i-1)
print(rst%1000000)
