import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int,input().split())
L = list(map(int,input().split()))
H = []
for idx, num in enumerate(L):
    #print(idx,num)
    while H and H[0][1]<=idx-K:
        heappop(H)
    heappush(H,(num,idx))
    print(H[0][0])
