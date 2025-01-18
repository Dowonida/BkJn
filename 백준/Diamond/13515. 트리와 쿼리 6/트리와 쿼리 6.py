import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def main():
    import sys

    input = sys.stdin.readline

    N = int(input()) + 2  # 0번 노드를 루트로 사용할 예정
    # 가상의 마지막노드도 존재

    adj = [[] for _ in range(N)]
    adj[0].append(1)  # 가상의 루트 노드

    for _ in range(N - 3):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    P = [0] * N  # parent 부모 노드의 번호
    D = [0] * N  # depth  노드의 depth
    E = [[0, 0] for _ in range(N)]  # euler 오일러경로 - 진입차수, 퇴장차수
    # 리프노드의 경우 진입차수 = 퇴장차수

    # 세그먼트 트리
    W = [0] * 2 * N  # weight 루트노드부터 자기까지의 경로에 있는 흰 정점 개수
    W[N] = 20000000
    R = [[0, 0] for _ in range(2 * N)]  # route 루트 개수 세그먼트 트리
    # 자신의 서브트리 내에서 경로 수
    # 자신은 무시하고 개수를 센다
    # end자리가 필요하다.
    # 변화량만 관리하자.

    L = [0] * N  # 초기 route값을 저장
    C = [0] * N  # 노드의 색

    def dfs(p=0, v=-1):
        v += 1
        E[p][0] = v
        cnt = 0
        for nxt in adj[p]:
            if D[nxt]: continue
            P[nxt] = p
            D[nxt] = D[p] + 1
            v, c = dfs(nxt, v)

            cnt += 1 + c
        E[p][1] = v
        L[p] = cnt

        return v, cnt

    dfs()

    PP = [P]  # LCA를 위한

    while True:
        flag = False
        temp = [0] * (N)
        for i in range(1, N):
            p = PP[-1][i]
            pp = PP[-1][p]
            if not pp:
                continue
            flag = True
            temp[i] = pp
        if not flag:
            break
        PP.append(temp)

    def get_pp(u):
        d = D[u]
        rst = u
        my_w = get_weight_from_root(u)

        for i in range(len(PP) - 1, -1, -1):

            p = PP[i][rst]
            if p == 0: continue
            p_w = get_weight_from_root(p)
            diff = d - D[p]
            assert my_w >= p_w

            if (my_w - p_w) == C[u] * diff and C[u] == C[p]:  # [0, diff]:
                rst = p
        return rst

    def get_weight_from_root(u):
        s = E[u][0] + N

        rst = 0

        while s:
            rst += W[s]
            s //= 2

        return rst

    def update_weight(u, val):
        s = E[u][0] + N
        e = E[u][1] + 1 + N
        while s < e:
            if s % 2:
                W[s] += val
                s += 1
            if e % 2:
                e -= 1
                W[e] += val
            s //= 2
            e //= 2

    def get_route(u):
        # u = get_pp(i)
        s = E[u][0] + N
        e = E[u][1] + N + 1
        s0 = s1 = e0 = e1 = 0
        while s:
            s0 += R[s][0]
            s1 += R[s][1]
            s //= 2
        while e:
            e0 += R[e][0]
            e1 += R[e][1]
            e //= 2

        return [e0 - s0 + L[u], e1 - s1]  # 흰색 경로 수, 검정 경로 수

    def update_route(u, v, val):
        # pp = PP[0][get_pp(u)]
        # pp = PP[1][u]

        # u~v노드 (u가 더 아래 노드) 구간에 업데이트
        v = PP[0][v]#get_pp(PP[0][v])
        s = E[v][0] + N + 1
        e = E[u][0] + N + 1
        while s < e:
            if s % 2:
                R[s][0] -= val[0]
                R[s][1] -= val[1]
                s += 1
            if e % 2:
                e -= 1
                R[e][0] -= val[0]
                R[e][1] -= val[1]
            s //= 2
            e //= 2


    for _ in range(int(input())):
        q, u = map(int, input().split())
        if q == 1:
            color = C[u]
            after = 1 - color
            p = PP[0][u]
            pp = get_pp(p)

            tmp = get_route(u)
            cut_before, add_after = tmp[color], tmp[after]

            # 부모노드부터 pp노드까지는 before색 개수가 cut_before+1만큼 감소
            # 부모노드의 경우


            diff2 = [0, 0]
            diff2[after] = add_after + 1
            diff1 = [0, 0]
            diff1[color] = -cut_before - 1

            if C[u] == C[p]: # 색이 부모와  달라지는 경우


                update_route(p, PP[0][pp], diff1)
                update_route(p, p, diff2)
            else:
                update_route(p, PP[0][pp], diff2)
                update_route(p, p, diff1)

            update_weight(u, after - color)
            C[u] = after

        else:
            pp = get_pp(u)
            color = C[u]

            print(get_route(pp)[color] + 1)


if True:
    main()
