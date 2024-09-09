import sys
import random
input = sys.stdin.readline

N = int(input())

#adj를 뒤집고 scc를 앞에서부터 처리
#같은 scc인 경우는 무시

#adj = [ [] for _ in range(N)]
default_input = {}
for _ in range(N):
    a, b, *c = input().split()
    default_input[a] = c


adj = {}
for i in default_input:
    if i not in adj: adj[i] = []
    for j in default_input[i]:
        if j not in adj: adj[j] = []
        adj[j].append(i)
    #adj[i] = [j for j in default_input[i] if j in default_input]


SCC = []
scc_num = {i:0 for i in adj}#[0]*N # fin
top = {i:0 for i in adj}#[0]*N
visited = {i:0 for i in adj}#[0]*N # dfs_n
cur_idx = {i:0 for i in adj}#[0]*N # adj[i]의 인덱스 

return_idx = {i:0 for i in adj}#[0]*N # 스택에서 되돌아갈 인덱스

for i in adj:#range(N):
    if scc_num[i]: continue

    visited[i] = 1
    top[i] = 1
    n_v = 2
    stk = [i]
    cur_stk_idx = 0 # 현재 스택 번호 
    while stk:
        cur = stk[cur_stk_idx]

        if cur_idx[cur] == len(adj[cur]):

            # cur 완료 처리
            if top[cur] == visited[cur]:
                # 내가 탑인 경우
                # 스택에서 내가 나올때까지 팝하면서 scc 생성
                scc = set()
                SCC.append(scc)
                cnt = len(SCC)
                while stk[-1]!=cur:
                    member = stk.pop()
                    scc_num[member] = cnt
                    scc.add(member)
                scc.add(stk.pop()) # cur이 나온다.
                scc_num[cur] = cnt
                cur_stk_idx = return_idx[cur]
                pass
            else:
                # 더 탑이 있는 경우
                # 부모노드로 이동
                cur_stk_idx = return_idx[cur] 
                pass
            continue
        
        nxt = adj[cur][cur_idx[cur]]
        if scc_num[nxt]:
            # nxt가 완료된 경우의 처리
            # 무시하고 다음 인덱스로
            cur_idx[cur] += 1
            continue
        if visited[nxt]:
            # nxt가 방문한 적이 있다면
            # 나의 top을 갱신하고 다음으로
            top[cur] = min(top[cur], top[nxt])
            cur_idx[cur] += 1
            continue
        # 첫 방문인 경우
        visited[nxt] = n_v
        top[nxt] = n_v
        n_v += 1
        return_idx[nxt] = cur_stk_idx

        cur_stk_idx = len(stk)
        stk.append(nxt)
        
            
score = {}
for i in adj:
    score[i] = 1


for scc in SCC[::-1]:
    for i in scc:
        if i not in default_input:continue
        for j in default_input[i]:
            if scc_num[i] == scc_num[j]:
                continue
            score[i] += score[j]
print(score[input().strip()])
    
