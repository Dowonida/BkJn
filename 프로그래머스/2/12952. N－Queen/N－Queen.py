def solution(n):
    answer = 0
    # R = [0]*n
    C = [0]*n
    PL = [0]*(2*n-1) #r+c 0~2*n-2
    ML = [0]*(2*n-1) #r-c -n+1~n-1
    
    def recur(r,c):
        if r == n-1:
            return 1
        C[c] = 1
        PL[r+c] = 1
        ML[r-c] = 1
        rst = 0
        for nc in range(n):
            if C[nc]:
                continue
            if PL[r+1+nc]:
                continue
            if ML[r+1-nc]:
                continue
            rst += recur(r+1,nc)
        C[c] = 0
        PL[r+c] = 0
        ML[r-c] = 0
        return rst
    rst = 0
    for i in range(n):
        rst += recur(0,i)
        
    
    return rst