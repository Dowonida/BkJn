case = 0
while True:
    case += 1

    n, m = map(int,input().split())
    if n==m==0:
        break

    #n개의 노드 m개의 간선

    visited = [0]*(n+1)

    adj = [ [] for _ in range(n+1)]
    rst = 0
    for i in range(m):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)


    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = 1
        V = [i]
        stk = [i]
        while stk:
            cur = stk.pop()
            for you in adj[cur]:
                if visited[you]:
                    continue
                stk.append(you)
                visited[you] = 1
                V.append(you)
        aaaaa = len(V)
        bbbbb = sum([ len(adj[x]) for x in V])
        if bbbbb == 2*aaaaa-2:
            rst += 1

    
    if rst == 0 :
        print(f'Case {case}: No trees.')
    elif rst == 1:
        print(f'Case {case}: There is one tree.')
    elif rst>1:
        print(f'Case {case}: A forest of {rst} trees.')
