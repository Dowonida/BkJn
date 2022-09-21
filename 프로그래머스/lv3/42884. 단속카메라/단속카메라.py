def solution(routes):
    answer = 0
    end=-50000
    routes.sort()
    for s,e in routes:
        if s<=end:
            end=min(e,end)
        else:
            answer+=1
            end=e
    return answer