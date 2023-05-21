from bisect import bisect_left as bs
import sys

input = sys.stdin.readline

N = int(input())
N = 1024*1024

seg = [[(0,0)] for _ in range(2*N)] #idx,val

idx_dic = {}

for idx,num in enumerate(map(int,input().split())):
    add_idx = N+idx
    sub_idx = 0
    if num in idx_dic:
        sub_idx = N+idx_dic[num]
    while sub_idx<add_idx:
        if sub_idx:
            seg[sub_idx].append((idx+1,seg[sub_idx][-1][1]-1))

        seg[add_idx].append((idx+1,seg[add_idx][-1][1]+1))

        sub_idx//=2
        add_idx//=2
    idx_dic[num] = idx
    
    
    
    
for _ in range(int(input())):
    a,b = map(int,input().split())
    sidx, eidx = a+N-1, N+N
    #bisect로 (a,0)을 찾기
    #seg[sidx][찾은인덱스][1]을 더하자
    rst = 0
    while sidx<eidx:
        if sidx%2:
            cntidx = bs(seg[sidx],(b+1,0))-1

            rst += seg[sidx][cntidx][1]
            sidx += 1
            


        if eidx%2:
            eidx -= 1
            cntidx = bs(seg[eidx],(b+1,0))-1

            rst += seg[eidx][cntidx][1]
            

        sidx//=2
        eidx//=2
    print(rst)
