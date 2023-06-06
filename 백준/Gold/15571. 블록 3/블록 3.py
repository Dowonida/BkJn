#키타마사 샘플코드 돌려보기 
def solve1(m, k, C, A):
    MOD = 1999
    C0 = [0]*k; C1 = [0]*k
    if m == 0:
        return A[0]
    C0[1] = 1

    def inc(k, C0, C1):
        C1[0] = C0[k-1] * C[0] % MOD
        for i in range(k-1):
            C1[i+1] = (C0[i] + C0[k-1]*C[i+1]) % MOD

    def dbl(k, C0, C1):
        D0 = [0]*k; D1 = [0]*k
        D0[:] = C0[:]
        for j in range(k):
            C1[j] = C0[0] * C0[j] % MOD
        for i in range(1, k):
            inc(k, D0, D1)

            for j in range(k):
                C1[j] += C0[i] * D1[j] % MOD
            D0, D1 = D1, D0
        for i in range(k):
            C1[i] %= MOD

    p = 32
    while (m >> p) & 1 == 0:
        p -= 1

    while p:
        p -= 1
        dbl(k, C0, C1)
        C0, C1 = C1, C0

        if (m >> p) & 1:
            inc(k, C0, C1)
            C0, C1 = C1, C0

    return sum(C0[i] * A[i] for i in range(k)) % MOD

N,M=map(int,input().split())
if N==1:
    print(1)
else:
    c=[1<<(N-1)]+[1]*(N-1)
    a=[1<<i for i in range(N-1)]+[(1<<N)-1]
    print(solve1(M-1,N,c,a))

