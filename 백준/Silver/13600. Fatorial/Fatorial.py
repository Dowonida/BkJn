N = int(input())

F = [1]

for i in range(2,10):
    F.append(i*F[-1])
    
rst = 0
for i in F[::-1]:
    rst += N//i
    N%=i
print(rst)
