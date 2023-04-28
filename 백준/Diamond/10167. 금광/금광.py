import sys
input = sys.stdin.readline


dic = {}
NN=16
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a not in dic:
        dic[a] = []
    dic[a].append((b+NN,c))

#전체합, 왼포맥, 오포맥, 전체맥
K = sorted(dic.keys())
N = len(K)
rst = 0

for i in range(N):
    seg = [ [0,0,0,0] for _ in range(NN*2)]
    for j in range(i,N):
        for idx,val in dic[K[j]]:
            for k in range(4):
                seg[idx][k] += val

            idx //= 2
            while idx:
                left, right = seg[idx*2], seg[idx*2+1]
                seg[idx] = [ left[0]+right[0],
                             max(left[1],left[0]+right[1]),
                             max(right[2],right[0]+left[2]),
                             max(left[3],right[3],left[2]+right[1])]
                idx //= 2
        rst = max(rst,seg[1][3])

print(rst)
                        
            
            
