

def solution(s,query):
    answer = []
    S = s
    A = 'abcdefghijklmnopqrstuvwxyz'
    N = len(s)

    M = len(query)
    P = {i:list(range(M)) for i in A} # P[i] : i번을 대표하는 원소의 번호. 최대 query수만큼임
    L = {i:list(range(M)) for i in A} # L[i] : i번 방에 실제로 있는 대표번호. 비어있으면 -1
    PP = {i:list(range(M)) for i in A}# PP[i]: i번 원소(대표)가 몇 번 방에 있는지 
    segs = {i:[0]*2*N for i in A}

    def move_a_to_b(char,before,after):
        # before방에 있는 모든 값을 after방으로 옮기기
        LL = L[char]
        before_prime = LL[before]
        after_prime = LL[after]
        if before_prime == -1:
            return # 시작방이 빈 경우 -> 덮어써지는게 없음
        elif after_prime == -1:
            L[char][after] = before_prime
            PP[char][before_prime] = after
            return # 도착방이 빈 경우 대표원소간의 union 필요없음
        else: # 둘 다 있는 경우
            prime = union(char, before_prime, after_prime)
            L[char][before] = -1
            L[char][after] = prime
            PP[char][prime] = after

    def union(char,a,b):
        p=P[char]
        pa = get(char,p[a])
        pb = get(char,p[b])
        pa,pb = sorted([pa,pb])
        P[char][pb]=pa # 작은 값을 대표로 
        return pa

    def get(char,a):
        p = P[char]
        pa = p[a]
        if pa != a:
            p[a] = get(char,pa)
        return p[a]
        

    def find_base_set(s_index):
        char = S[s_index]

        seg = segs[char]
        rst = 0
        idx = s_index + N
        while idx:
            rst = max(rst,seg[idx])
            idx//=2
        return rst
    def find_prime_set(s_index):
        char = S[s_index]
        rst = find_base_set(s_index)
        prime = get(char,rst)
        return prime
    # seg -> find -> place해야 현재 위치
    def find_my_place(s_index):
        char = S[s_index]

        seg = segs[char]
        rst = 0
        idx = s_index + N
        while idx:
            rst = max(rst,seg[idx])
            idx//=2
        prime = get(char,rst)
        return PP[char][prime]
        
    
    next_idx = 1

    for q in query:
        q, *Q = q.split()
        if q=='1':
            x = int(Q[0])-1
            y = int(Q[1])-1
            px = find_my_place(x)
            py = find_my_place(y)
            if px == py:
                answer.append("YES")
            else:
                answer.append("NO")

        elif q=='2':
            x = int(Q[0])-1
            word = set(Q[1])
            px = find_my_place(x)
            pn = next_idx
            next_idx += 1
            for w in word:
                move_a_to_b(w, px,pn)
                
        elif q=='3':
            x = int(Q[0])-1
            y = int(Q[1])-1
            word = set(Q[2])
            pn = next_idx
            next_idx += 1

            sidx = x+N
            eidx = y+N+1
            while sidx<eidx:
                if sidx%2:
                    for c in word:
                        segs[c][sidx] = pn
                    sidx += 1
                if eidx%2:
                    eidx -=1
                    for c in word:
                        segs[c][eidx] = pn
                sidx//=2
                eidx//=2
    
        elif q=='4':
            x = int(Q[0])-1
            y = int(Q[1])-1
            px = find_my_place(x)
            py = find_my_place(y)

            ax,bx = sorted([px,py])

            for c in A:
                move_a_to_b(c,bx,ax)
            
        else:
            RST = {} # place : {alph:alph_count}
            for i in range(N):
                char = S[i]
                p = find_my_place(i)
                if p not in RST:
                    RST[p] = {}
                if char not in RST[p]:
                    RST[p][char] = 0
                RST[p][char] += 1

            for i in range(next_idx+1):
                if i not in RST:
                    continue
                rst = RST[i]
                tmp = [f'{i} {rst[i]}' for i in A if i in rst]
                answer.append(' '.join(tmp))


    return answer
