import sys
input = sys.stdin.readline

N, M = map(int,input().split()) #M마다  밤낮 바뀜




date = 1
sun = 1 #2가 밤, 1이 낮
turn = 0
#0~M-1턴이 낮

Map = [[2]*(N+2)]
visited1 = [[1023]*(N+2)]
visited2 = [[1023]*(N+2)]
for i in range(N):
    Map.append([1023]+list(map(int,input().split()))+[1023])
    visited1.append( [1023]+[0]*N+[1023])
    visited2.append( [1023]+[0]*N+[1023])
Map.append([1023]*(N+2))
visited1.append([1023]*(N+2))
visited2.append([1023]*(N+2))
#밤에 방문한 점을 굳이 낮에 방문할 필요 없음
#visited=0 미방문, 1=낮방문 2=밤방문
#visited값이 더 낮은 경우만 갈 수 있음
SUNMOON=[0,'sun','moon']

que = [(1,1)]
dr = [1,-1,0,0]
dc = [0,0,-1,1]


while que:
    nq = []
    if turn == M:
        turn=0
        sun = 3-sun #2가 밤 1이 낮
        if sun ==1:#새로운 낮
            date += 1

    for r,c in que:
        if r==c==N:
            print(date, SUNMOON[sun])
            nq=[]
            break
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if sun==1 and not(visited1[nr][nc]&(1<<turn)):
                if Map[nr][nc] == 0:
                    visited1[nr][nc] += (1<<turn)
                    nq.append( (nr,nc))

            elif sun==2:
                while Map[nr][nc]==1:
                    nr+=dr[i]
                    nc+=dc[i]
                if not(visited2[nr][nc]&(1<<turn)):
                    visited2[nr][nc]+= (1<<turn)
                    nq.append( (nr,nc))

    else: #r,c가 끝남

        que = nq
        turn += 1
        continue
    break


else:
    print(-1)
