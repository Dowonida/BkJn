def solution(food_times, k):
    answer = 0
    L=len(food_times)
    
    yang={i:[] for i in sorted(food_times)}
    for i in range(L):
        yang[food_times[i]].append(i)
    Y=sorted(list(yang.keys())) # Y=[1,2,3]
    food_times=[-100]+food_times
    if Y[0]*L>=k:
        k%=L
        return k+1
    cnt=L-len(yang[Y[0]])#남은 음식 수
    time=Y[0]*L
    for i in range(1,len(Y)):
        time+= cnt*(Y[i]-Y[i-1])
        if time>k:
            time-=cnt*(Y[i]-Y[i-1])
            break
        cnt-=len(yang[Y[i]])
    else:
        return -1
    answer=[j for j in range(1,1+L) if food_times[j]>=Y[i] ][(k-time)%cnt]
    return answer