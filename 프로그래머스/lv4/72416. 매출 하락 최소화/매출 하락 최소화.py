def tree(n,sales):
    global DP, dic
    if DP[n]!=-1: #저장이되어있으면 가져다쓰기
        return DP[n]
    if not dic[n]:#리프노드면 끝자락 
        DP[n]=0
        return DP[n]
    
    sons=dic[n]
    M=sales[n]+sum( tree(i,sales) for i in sons)
    A=min( sales[i]+ (sum(tree(j,sales) for j in sons+dic[i] if j!=i)) for i in sons)
    DP[n]=min(A,M)
    return DP[n]

def solution(sales, links):
    global DP, dic
    answer = 0
    sales=[0]+sales
    DP=[-1]*len(sales)#메모이제이션 
    dic={i:[] for i in range(len(sales))}
    for a,b in links:
        dic[a].append(b)
    return tree(1,sales)