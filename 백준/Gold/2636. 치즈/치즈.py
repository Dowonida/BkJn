import sys
input = sys.stdin.readline

R, C = map(int,input().split())

Map = [list(map(int,input().split())) for _ in range(R)]


# 주변 턴의 min순 2번째값 +1이 방문
visited = [ [0]*(C) for _ in range(R)]


que = { (0,0)}
wait = { (0,0)}
end_count = 0
turn = -1
while wait:
    que = wait
    end_count = len(wait)
    wait = set()
    turn += 1
    while que:
        nq = set()
        for r,c in que:
            npos=[]
            if r>0:
                npos.append( (r-1,c))
            if r<R-1:
                npos.append((r+1,c))
            if c>0:
                npos.append( (r,c-1))
            if c<C-1:
                npos.append((r,c+1))
            for nr, nc in npos:
                if visited[nr][nc]:
                    continue
                if Map[nr][nc]==0:
                    nq.add((nr,nc))
                    visited[nr][nc] = 1
                else:
                    Map[nr][nc] -= 1
                    if Map[nr][nc] ==0:
                        visited[nr][nc] = 1
                        wait.add((nr,nc))
        que = nq

    
print(turn)
print(end_count)
