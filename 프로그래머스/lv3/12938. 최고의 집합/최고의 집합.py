def solution(n, s):
    a=s//n
    
    answer = [a]*(n-s%n) +[a+1]*(s%n)
    if answer[0]==0:
        answer=[-1]
    return answer