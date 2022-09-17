def solution(n, lost, reserve):
    N=[1]*n
    for i in lost:
        N[i-1]-=1
    for i in reserve:
        N[i-1]+=1
    for i in range(n):
        if i>0:
            if N[i]>1 and N[i-1]==0:
                N[i]-=1
                N[i-1]+=1
        if i<n-1:
            if N[i]>1 and N[i+1]==0:
                N[i]-=1
                N[i+1]+=1
    answer = n-N.count(0)
    return answer