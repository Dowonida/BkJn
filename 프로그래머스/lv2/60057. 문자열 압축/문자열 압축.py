def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        
        a = len(s)
        cnt=1
        for j in range(0,len(s),i):
            if j==0 or s[j:j+i]!=s[j-i:j]:
                if cnt>1:
                    a+=len(str(cnt))
                cnt=1
                
            else:#같을 경우
                cnt+=1
                a-=i
        if cnt>1:
            a+=len(str(cnt))
        answer=min(answer,a)
    return answer