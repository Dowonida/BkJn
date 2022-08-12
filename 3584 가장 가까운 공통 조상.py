import sys
input=sys.stdin.readline

T=int(input())

for test_case in range(T):
    N = int(input())
    dic={}
    root={i for i in range(1,N+1)}
    for i in range(N-1):
        a,b=map(int,input().split())
        dic[b]=a
        root.discard(b)
    root=root.pop()
    m1,m2=map(int,input().split())
    M1={m1}
    while root not in M1:
        m1=dic[m1]
        M1.add(m1)

    while m2 not in M1:
        m2=dic[m2]
    print(m2)
