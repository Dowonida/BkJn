def solution(record):
    answer = []
    dic={}
    cs=[]
    for i in record:
        x=i.split()
        a=x[0]
        b=x[1]
        if a!="Leave":
            c=x[2]
        if a=="Enter":
            cs.append([b,"님이 들어왔습니다."])
            dic[b]=c
        elif a=="Change":
            dic[b]=c
        elif a=="Leave":
            cs.append([b,"님이 나갔습니다."])
    
    for a,b in cs:
        answer.append(f'{dic[a]}{b}')
    
    
    return answer