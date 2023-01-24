import sys
input = sys.stdin.readline


# L = 0
# R = 1

N, M = map(int,input().split())

cnt = 1
while cnt<N:
    cnt *= 2

seg = [0]*cnt + [[ 1,1,1,0,0,1] for _ in range(N)]+[ [0,0,0,-1,-1,0] for _ in range(cnt-N)]
N = cnt

#전체최대길이, 왼쪽포함 최대길이, 오른쪽포함 최대길이
#왼쪽 끝 좌우, 오른쪽끝 좌우, 전체 길이

#전체 길이 = max(좌전체길이, 우전체길이)
#만약 좌 우끝과 우 좌끝이 다르면 좌 우포함길이+우 좌포함길이도 넣어서 max

#왼쪽포함 최대길이 = 왼쪽의 왼쪽포함 최대길이
#만약 왼쪽의 우끝과 오른쪽의 좌끝이 같고, 왼쪽의 왼최대길이가 전체길이와 같으면
#왼쪽포함 최대길이 += 오른쪽의 왼포함길이

#왼쪽끝 인덱스는 왼쪽거를 가져옴

def merge(Lidx, Ridx):

    L = seg[Lidx]
    R = seg[Ridx]
    rst = [0]*6
    rst[3] = L[3]
    rst[4] = R[4]
    rst[5] = L[5]+R[5]

    cnt = 0
    cntl = 0
    cntr = 0
    if L[4] == 1-R[3]:
        cnt = L[2]+R[1]
        if L[1] == L[5]:
            cntl = L[1]+R[1]
        if R[2] == R[5]:
            cntr = R[2]+L[2]
    rst[0] = max(L[0],R[0],cnt)
    rst[1] = max(L[1],cntl)
    rst[2] = max(R[2],cntr)

    return rst

for i in range(N-1,0,-1):
    seg[i] = merge(i*2,i*2+1)


for _ in range(M):
    idx = int(input())+ N-1
    seg[idx][3]=seg[idx][4] = 1-seg[idx][3]
    idx //= 2
    while idx:
        
        seg[idx] = merge(idx*2,idx*2+1)
        idx //=  2
    print(seg[1][0])
    

    
