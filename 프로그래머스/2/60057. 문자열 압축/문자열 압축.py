def solution(s):
    
    answer = len(s)
    for i in range(1,len(s)//2+1):
        stk = [[1,'']]
        rst = 0
        for j in range(0,len(s),i):
            ss = s[j:j+i]
            if ss == stk[-1][1]:
                stk[-1][0] += 1
            else:
                rst += len(stk[-1][1])+(len(str(stk[-1][0])) if stk[-1][0]!=1 else 0)
                stk.append([1,ss])
        
        rst += len(stk[-1][1])+(len(str(stk[-1][0])) if stk[-1][0]!=1 else 0)
        answer = min(answer,rst)
    
    return answer