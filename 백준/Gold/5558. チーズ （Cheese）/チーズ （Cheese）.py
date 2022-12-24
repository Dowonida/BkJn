import sys
input = sys.stdin.readline

R, C, N = map(int,input().split())

Map = [ input().strip()+'X' for _ in range(R)]
Map.append('X'*(C+1))
visited = [ [-1]*C for _ in range(R) ]

def find_start(R,C,Map):
    dic = {}
    for i in range(R):
        for j in range(C):
            if Map[i][j] not in '.X':
                dic[Map[i][j]] = (i,j)
    return dic


dic = find_start(R,C,Map)
dic['0'] = dic['S']


rst = 0

for i in range(N):
    que = { dic[str(i)]}
    
    while que:
        nq = set()
        rst += 1
        for cur_r, cur_c in que:
            

            for nr, nc in [(cur_r-1,cur_c),(cur_r+1,cur_c)
                           ,(cur_r,cur_c-1),(cur_r,cur_c+1)]:
                if Map[nr][nc] == 'X' or visited[nr][nc]==i:
                    continue
                if Map[nr][nc] == str(i+1):
                    nq = {}

                    break
                visited[nr][nc] = i
                nq.add( (nr,nc) )
            else:
                continue
            break
                
        que = nq

print(rst)
