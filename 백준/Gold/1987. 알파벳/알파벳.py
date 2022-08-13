import sys
input=sys.stdin.readline


def solve():

    R, C = map(int, input().split())
    length = R * C
    visited = [set() for _ in range(length)]

    arr = [0] * length
    for i in range(R):
        arr[i * C:(i+1) * C] = [*map(lambda char: 1 << (ord(char) - 65), input().strip())]
    ans = 0
    que = {0}
    visited[0].add(arr[0])
    for k in range(27):
        if k == 26 or not que:#더 갈 곳 없거나 26찍으면 탈출 while대신 for문을 쓴듯. 어차피 그 이상안할테니 근데 왜 bfs?
            ans = k
            break
        new_que = set()
        new_visited = [set() for _ in range(length)]
        while que:
            cur_pos = que.pop()
            adj=set()
            cur_r = cur_pos//C
            cur_c = cur_pos%C
            if cur_r>0:
                adj.add(cur_pos-C)
            if cur_c>0:
                adj.add(cur_pos-1)
            if cur_r<R-1:
                adj.add(cur_pos+C)
            if cur_c<C-1:
                adj.add(cur_pos+1)

            for NP in adj:
                NA=arr[NP]
                for mover in visited[cur_pos]:
                    if not NA&mover:
                        new_que.add(NP)
                        new_visited[NP].add(NA|mover)
        que=new_que
        visited=new_visited
    return ans


print(solve())