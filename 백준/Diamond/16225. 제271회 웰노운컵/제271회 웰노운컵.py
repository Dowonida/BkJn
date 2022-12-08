from heapq import heappop, heappush
N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [A[i] for i in sorted(range(N), key= lambda x: B[x], reverse=True)]

D = []
for i in range(1,N-1,2):
    heappush(D,C[i])
    heappush(D,C[i+1])
    heappop(D)
print(sum(D)+C[-1])
