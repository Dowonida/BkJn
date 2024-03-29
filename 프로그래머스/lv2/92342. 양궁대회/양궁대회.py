def solution(n, info):
    Ap= -sum([(10-i) for i in range(11) if info[i]>0])
    Bp= Ap
    #print(Bp)
    need=[]
    for i in info:
        need.append(i+1)
        
    answers = []
    que=[]
    # (idx,score,visited)
    for i in range(2048):
        visited=[ (bool((2**j)&i))*need[j] for j in range(11)]
        if sum(visited)>n:
            continue
        
        score=0
        for i in range(11):
            if visited[i]:
                score+=10-i
            elif info[i]:
                score-=10-i
        if score>Bp:
            Bp=score
            rest=n-sum(visited)
            visited[-1]+=rest
            answers=[visited]
        elif score==Bp:
            rest=n-sum(visited)
            visited[-1]+=rest
            answers.append(visited)
        
    if Bp<=0:
        return [-1]
    return answers[-1]