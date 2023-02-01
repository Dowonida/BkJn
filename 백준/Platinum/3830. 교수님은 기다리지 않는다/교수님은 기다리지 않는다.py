import sys

input = sys.stdin.readline



while True:
    N, M = map(int,input().split())
    if N==M==0:
        break
    rep = [i for i in range(N+1)]
    diff = [0]*(N+1) #대표원소로부터 차이
    for _ in range(M):
        
        A = input().split()
        if A[0] == '!':
            a,b,c = map(int,A[1:])
            da = 0
            db = 0
            stk = []
            while True:

                if a != rep[a]:
                    stk.append(a)
                    a = rep[a]
                else:
                    Ra = a
                    while stk:
                        prev = stk.pop()
                        rep[prev] = Ra
                        da += diff[prev]
                        diff[prev] = da

                    break
            
            while True:
                
                if b != rep[b]:
                    stk.append(b)
                    b = rep[b]
                else:
                    Rb = b
                    while stk:
                        prev = stk.pop()
                        rep[prev] = Rb
                        db += diff[prev]
                        diff[prev] = db
                        

                    break
            rep[Rb] = Ra
            diff[Rb] = da+c-db
        else:
            a,b = map(int,A[1:])
            oa = a
            ob = b
            da = 0
            db = 0
            stk = []
            while True:

                if a != rep[a]:
                    stk.append(a)
                    a = rep[a]
                else:
                    Ra = a
                    while stk:
                        prev = stk.pop()
                        rep[prev] = Ra
                        da += diff[prev]
                        diff[prev] = da

                    break
            
            while True:
                
                if b != rep[b]:
                    stk.append(b)
                    b = rep[b]
                else:
                    Rb = b
                    while stk:
                        prev = stk.pop()
                        rep[prev] = Rb
                        db += diff[prev]
                        diff[prev] = db
                    break
            if Ra!=Rb:
                print("UNKNOWN")
            else:
                print(diff[ob]-diff[oa])
