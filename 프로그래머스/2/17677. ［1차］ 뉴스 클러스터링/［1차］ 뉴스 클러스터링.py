def solution(str1, str2):
    strs = [str1.lower(), str2.lower()]
    ss = [{},{}]
    for i in range(2):
        for j in range(len(strs[i])-1):
            s = strs[i][j:j+2]
            if not s.isalpha(): continue
            if s not in ss[i]: ss[i][s] = 0
            if s not in ss[1-i]: ss[1-i][s] = 0
            ss[i][s] += 1
    
    bj = bm = 0
    for i in ss[0]:
        cnt = sorted((ss[0][i], ss[1][i]))
        bj += cnt[0]
        bm += cnt[1]
    return int(65536*bj/bm) if bm else 65536
        
    