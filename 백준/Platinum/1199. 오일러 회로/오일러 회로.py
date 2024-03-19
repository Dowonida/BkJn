import sys
input = sys.stdin.readline

def main():
    N = int(input())

    adj = [{} for _ in range(N+1)]
    for i in range(1,N+1):
        con = 0 #i노드에 연결된 간선 수 
        cnt = [0]+list(map(int,input().split()))
        for j in range(1,N+1):
            if cnt[j]:
                adj[i][j] = cnt[j]
                con += cnt[j]
        if con%2: #하나라도 홀수 간선이면 탈출
            print(-1)
            return 


    rst = []
    stk = [1] #스택에 dfs로 담다가 더 갈 곳 없으면 rst에 넣기
    while stk:

        node = stk[-1]
        #만약 갈 곳이 없으면 pop해서 rst에 넣어야 함
        if not adj[node]:
            rst.append(stk.pop())
            continue

        for node2 in adj[node]:
            break

        stk.append(node2)
        adj[node][node2] -= 1
        adj[node2][node] -= 1
        if adj[node][node2] == 0:
            del(adj[node][node2])
            del(adj[node2][node])
    print(' '.join(map(str, rst)))
    

main()