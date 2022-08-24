from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer=0
    heapify(scoville)
    while True:
        

        a=heappop(scoville)
        if a>=K:
            return answer
        if len(scoville)==0:
            return -1
        b=heappop(scoville)
        heappush(scoville,a+2*b)
        answer+=1
        
    
    
    return answer