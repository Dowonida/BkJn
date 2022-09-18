def solution(citations):
    citations=[-1]+sorted(citations, reverse=True)
    answer=0
    for i in range(1,len(citations)):
        answer=max(answer,min(i,citations[i]))
    return answer