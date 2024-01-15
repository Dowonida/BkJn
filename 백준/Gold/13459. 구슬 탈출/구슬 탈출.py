R, C = map(int,input().split())


Map = [list(input()) for _ in range(R)]
for r in range(R):
    for c in range(C):
        if Map[r][c] == 'B':
            br, bc = r,c
            Map[r][c] = '.'
        if Map[r][c] == 'R':
            rr, rc = r,c
            Map[r][c] = '.'
        if Map[r][c] == 'O':
            gr, gc = r,c
            Map[r][c] = '.'
        



def move(self, other, vector):
    # self = (rr, rc)
    # other = (br, bc)
    # 현 위치가 구멍이면 return -1, -1
    # 다음 위치가 벽이나 상대면 return 현위치
    sr, sc = self
    tr, tc = other
    dr, dc = vector

    while True:
        if (sr,sc) == (gr,gc):
            return -1, -1

        nr, nc = sr+dr, sc+dc
        if Map[nr][nc] == '#' or ((nr,nc) == (tr,tc)):
            return sr, sc
        sr, sc = nr, nc

def move_all(rr,rc, br,bc, dr,dc):
    R = -rr*dr-rc*dc
    B = -br*dr-bc*dc
    if R<B:
        rr,rc = move((rr,rc),(br,bc),(dr,dc))
        br,bc = move((br,bc),(rr,rc),(dr,dc))
    else:
        br,bc = move((br,bc),(rr,rc),(dr,dc))
        rr,rc = move((rr,rc),(br,bc),(dr,dc))

    return rr,rc, br,bc
            
def main(rr,rc, br,bc, gr,gc):
    visited = {(rr,rc, br,bc)}
    que = [(rr,rc,br,bc,0)]
    for rr,rc, br,bc, t in que:
        if (br,bc) == (-1,-1):
            continue
        if (rr,rc) == (-1,-1):
            return 1
        if t == 10:
            continue
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nrr, nrc, nbr, nbc = move_all(rr,rc,br,bc,dr,dc)
            if (nrr,nrc,nbr,nbc) in visited:
                continue
            visited.add((nrr,nrc,nbr,nbc))
            que.append((nrr,nrc,nbr,nbc,t+1))
    return 0
print(main(rr,rc, br,bc, gr,gc))       
