import sys
input = sys.stdin.readline

N = int(input())
L = [int(input()) for _ in range(N)]
L = sorted(L)

M = [L[i+1]-L[i] for i in range(len(L)-1)]

gcd = 0

for i in M:
    while i:
        i, gcd = gcd%i, i

rst1 = []
rst2 = [str(gcd)]
for i in range(2,int(gcd**0.5)+1):
    if gcd%i:
        continue
    rst1.append(str(i))
    if gcd//i != i:
        rst2.append(str(gcd//i))

print(' '.join(rst1+rst2[::-1]))
