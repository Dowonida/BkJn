import sys
input = sys.stdin.readline
def main(M,Map):

    
    Range = range(1,M+1)
    Vector = [(0,1),(0,-1),(1,0),(-1,0)]
    sr, sc, er, ec = map(int,input().split())

    que = { (sr,sc) }
    Map[sr][sc] = 0
    turn = 0
    while que:
        turn += 1
        nq = set()
        for cur_r, cur_c in que:
            for vr, vc in Vector:
                for i in Range:
                    nr = cur_r+vr*i
                    nc = cur_c+vc*i
                    if Map[nr][nc]<turn:
                        break
                    Map[nr][nc] = turn
                    nq.add( (nr,nc) )
                    if (nr,nc) == (er,ec):
                        return turn

        que = nq
    return -1

R, C, M = map(int,input().split()) #행,열,점프
Max = 1000000
Map =  [[ 0 for _ in range(C+2)]] #상단 패딩
dic = {'.':Max, '#':0} 
for i in range(R):
    Map.append( [0]+list(map(lambda x: dic[x],input().strip()))+[0])
Map.append( [0 for _ in range(C+2)])


print(main(M,Map))