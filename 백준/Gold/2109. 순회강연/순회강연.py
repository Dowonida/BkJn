
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
data = sorted( (tuple(map(int,input().split())) for _ in range(N)), key = lambda x: -x[1])
data.append( (0,0) )
N += 1
rst = 0
H = []
data_idx = 0
date = 100000
while data_idx<N:
    today = data[data_idx][1]

    
    for i in range(date-today):
        if H:
            rst -= heappop(H)
        else:
            break
    date = today
    while data_idx<N and data[data_idx][1]==date:
        heappush(H,-data[data_idx][0])
        data_idx += 1

print(rst)
