import sys
input = sys.stdin.readline

N, K = map(int,input().split())

Map = [ list(map(int,input().split()))+[-1] for _ in range(N) ]
Map.append ( [-1]*(N+1))

S, R, C = map(int,input().split())
C -= 1
R -= 1

que = {(R,C)}
V = set()
for i in range(S+1):
    nq = set()
    for r,c in que:
        if Map[r][c]:
            V.add(Map[r][c])
        else:
            Map[r][c] = -1

            for nr, nc in ( (r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if Map[nr][nc]>=0:
                    nq.add ((nr,nc))
    if V:
        break

    que = nq

if V:
    print(min(V))
else:
    print(0)
