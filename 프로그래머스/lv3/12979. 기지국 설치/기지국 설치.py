def solution(n, stations, w):
    answer = 0
    start=1 #0이 시작되는 점. 인덱스가 1부터이므로 1로 시작
    for i in stations:
        #i-w가 1인 가장 왼쪽 점
        start=min(i-w,start) #0인 가장 왼쪽점
        answer+= (i-w-start)//(2*w+1)+bool((i-w-start)%(2*w+1))
        start=i+w+1
    
    start=min(n+1,start)
    answer+= (n+1-start)//(2*w+1)+bool((n+1-start)%(2*w+1))
    return answer