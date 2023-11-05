import sys
input = sys.stdin.readline

def gcd(a,b):
    while a:
        a,b = b%a, a
    return b
def get(a,b):
    if a>b:
        a,b = b,a
    return dic[(a,b)]
dic = {}
for i in range(1,101):
    for j in range(i,101):
        dic[(i,j)] = gcd(i,j)

while True:
    N = int(input())
    if not N:
        break
    S = set()
    L = []
    for i in range(N):
        n = int(input())
        if L and L[-1]==n:
            continue
        L.append(n)
        S.add(n)
    while L:
        nL = []
        for i in range(1,len(L)):
            n = get(L[i-1],L[i])
            if L and L[-1] == n:
                continue
            nL.append(n)
            S.add(n)
        L = nL
    print(len(S))
