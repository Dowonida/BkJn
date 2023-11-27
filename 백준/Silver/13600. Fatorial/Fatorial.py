N = int(input())

L = [0]*(100001)
F = []
cnt = 1
for i in range(2,10):
    F.append(cnt)
    L[cnt] = 1
    cnt *= i
rst = 0
for i in F[::-1]:
    rst += N//i
    N%=i
print(rst)
