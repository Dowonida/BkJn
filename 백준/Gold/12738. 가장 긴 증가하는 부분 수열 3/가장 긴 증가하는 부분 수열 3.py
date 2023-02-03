import sys
input = sys.stdin.readline
import bisect

N = int(input())
L = list(map(int,input().split()))

stk = []

for i in L:
    idx = bisect.bisect_left(stk,i)
    if idx == len(stk):
        stk.append(i)
    else:
        stk[idx] = i
print(len(stk))
