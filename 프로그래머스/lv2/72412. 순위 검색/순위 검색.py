import bisect

def solution(info, query):
    answer=[]
    for i in range(len(info)):
        info[i]=info[i].split()
        info[i][4]=int(info[i][4])
    N=len(info)
    S={i for i in range(N)}
    
    kwd=['cpp','java','python','backend','frontend','junior','senior','chicken','pizza']
    dic = {i:set() for i in kwd}
    DP = {}
    for i in range(N):
        for j in range(4):
            dic[info[i][j]].add(i)
    
    for i in query:
        i=i.replace('and ','').replace('-','').split()
        i[-1]=int(i[-1])
        j=tuple(i[:-1])
        if j not in DP:
            A=S.copy()
            for k in i[:-1]:
                A&=dic[k]
            A=sorted(A, key= lambda x: info[x][-1])
            DP[j]=[ info[i][-1] for i in A]
        A=DP[j]
        n=bisect.bisect_left(A,i[-1])
        answer.append(len(A)-n)
    return answer