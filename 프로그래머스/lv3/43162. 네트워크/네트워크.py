def union(a,b):
    x=get(a)
    y=get(b)
    if x<y:
        dic[y]=x
    else:
        dic[x]=y
def get(x):
    if dic[x]==x:
        return x
    else:
        dic[x]=get(dic[x])
        return dic[x]
    
def solution(n, computers):
    global dic
    answer=n
    dic={i:i for i in range(n)}
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] and get(i)!=get(j):
                answer-=1
                union(i,j)
    return answer