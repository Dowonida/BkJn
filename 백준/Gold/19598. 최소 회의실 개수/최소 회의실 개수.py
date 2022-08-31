from heapq import heappop, heappush, heapify
import sys
input=sys.stdin.readline
#처음 코드에서 개선된 부분
#readline을 빼먹어서 넣음 !!가장 기본적인 부분이었는데..
#M을 리스트인 상태에서 정렬하는 방법과 다 만들고 heapify하는 방법을 비교해봤는데
#다 만들고 heapify할 바에는 heappush를 하는게 나음
#***heappop을 안해도 0번 원소가 가장 우선순위라서 바로 비교가 가능

N= int(input())
M = []

for i in range(N):
    b,c=map(int,input().split())
    heappush(M,(b,c))


stack=[0]

while M:
    if stack[0]<=M[0][0]:
        heappop(stack)
        heappush(stack,heappop(M)[1])
    else:
        heappush(stack,heappop(M)[1])
        
        
print(len(stack))
