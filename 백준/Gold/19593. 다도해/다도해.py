#19593 다도해
import sys
input = sys.stdin.readline

def union(a,b):
    a = find(a)
    b = find(b)
    a,b = sorted([a,b])
    dic[b] = a

def find(a):
    stk = []
    while a != dic[a]:
        stk.append(a)
        a = dic[a]
    for i in stk:
        dic[i] = a
        
    return dic[a]


for _ in range(int(input())):
    N, seed, A, B = map(int,input().split())
    con = 0
    dic = [i for i in range(N)]
    day = 0
    seed = seed%(N*N)
    while con<N-1:
        X = find(seed//N)
        Y = find(seed%N)
        if X!=Y:
            union(X,Y)
            con += 1
            
            

        
        seed = (seed*A+B)%(N*N)
        day += 1
        if day == N*N:
            print(0)
            break
    else:
        print(day)
