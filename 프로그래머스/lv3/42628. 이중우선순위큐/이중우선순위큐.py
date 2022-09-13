def solution(operations):
    
    
    answer = []
    flag=True
    idx=0
    for i in operations:
        a,b=i.split()
        b=int(b)
        if a=='I':
            flag=False
            answer.append(b)
        elif a=='D':
            if flag==False:
                answer.sort()
                flag=True
            if idx<len(answer):
                if b==-1:
                    idx+=1
                elif b==1:
                    answer.pop()
    if idx<len(answer):
        answer.sort()
        answer=[answer[-1],answer[idx]]
    else:
        answer=[0,0]
            
            
    return answer