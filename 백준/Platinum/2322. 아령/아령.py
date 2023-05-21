import sys
input = sys.stdin.readline


N = int(input())
L = list(map(int,input().split()))
S = sorted(L)
dic = { L[i]:i for i in range(N)}

rst = 0
M = S[0]
for i in range(N):
    mini = S[i]

    idx = dic[mini]
    cnt = 1
    while idx!=i:
        cnt += 1
        num = S[idx]
        idx = dic[num]
        
    
    if mini*(cnt-1)>mini*2+M*(cnt+1):
        dic[mini], dic[M] = dic[M], dic[mini]
        rst += mini+M
        mini = M
        i = 0

    while dic[mini]!=i:
        #mini의 현재위치와 현재위치에 원래 있어야하는 친구
        #mini의 현재위치는 dic[mini]
        #현재위치에 있어야하는친구는 S[i]
        #둘의 인덱스를 바꿔야함
        cur_pos = dic[mini]
        nxt_num = S[cur_pos]
        nxt_pos = dic[nxt_num]
        dic[mini],dic[nxt_num] = nxt_pos, cur_pos
        rst += mini+nxt_num
print(rst)
        
