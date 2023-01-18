N = int(input())+1

seg = [0]*(N+1)+list(map(int,input().split()))

for _ in range(int(input())):
    Q = map(int,input().split())
    if next(Q) == 1:
        i, j, k = Q
        s = i+N
        e = j+N+1
        while s<e:
            if s%2:
                seg[s] += k
                s += 1
            if e%2:
                e -= 1
                seg[e] += k
            s //= 2
            e //= 2


    else:
        idx, = Q
        idx += N
        rst = 0
        while idx:
            rst += seg[idx]
            idx //= 2
        print(rst)
