import sys
input = sys.stdin.readline
import bisect

N = int(input())
L = list(map(int,input().split()))

stk = [-10000000000]
cnt = 1
for i in L:

    if i>stk[-1]:
        stk.append(i)
        if cnt<len(stk):
            cnt *= 2
        continue
    idx = cnt
    rst = 0
    while idx:
        nrst = rst + idx
        if nrst >= len(stk):
            idx //= 2
        elif stk[nrst-1]>=i:
            idx //= 2
        else:
            rst += idx
    stk[rst] = i
    
    #print(stk)
print(len(stk)-1)
