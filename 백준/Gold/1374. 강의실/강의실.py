from heapq import heappop, heappush, heapify
import sys
input=sys.stdin.readline

N= int(input())

C = [0]*N
M = []
for i in range(N):
    a,b,c=map(int,input().split())
    M.append((b,c))
heapify(M)
stack=[0]

while M:
    i=heappop(M)
    a=heappop(stack)
    if a<=i[0]:
        heappush(stack,i[1])
    else:
        heappush(stack,i[1])
        heappush(stack,a)

print(len(stack))
