from heapq import heappop, heappush, heapify
N= int(input())

C = [0]*N
M = []
for i in range(N):
    a,b,c=map(int,input().split())
    M.append((b,c))
heapify(M)

rst=1#최소한 1개는 있어야지
stack=[0]

while M:
    i=heappop(M)
    a=heappop(stack)
    if a<=i[0]:
        heappush(stack,i[1])
    else:
        heappush(stack,i[1])
        heappush(stack,a)
        rst=max(rst,len(stack))
print(rst)
