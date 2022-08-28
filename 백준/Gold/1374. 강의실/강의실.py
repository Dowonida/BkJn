from heapq import heappop, heappush, heapify
import sys
input=sys.stdin.readline

N= int(input())
M = []

for i in range(N):
    a,b,c=map(int,input().split())
    heappush(M,(b,c))


stack=[0]

while M:
    if stack[0]<=M[0][0]:
        heappop(stack)
        heappush(stack,heappop(M)[1])
    else:
        heappush(stack,heappop(M)[1])
        
        
print(len(stack))
