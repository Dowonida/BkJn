def time_to_num(STR):
    a,b,c=map(int,STR.split(":"))
    return a*3600+60*b+c
def num_to_time(num):
    a=num//3600
    num-=a*3600
    b=num//60
    c=num%60
    a=str(a)
    b=str(b)
    c=str(c)
    if len(a)<2:
        a='0'+a
    if len(b)<2:
        b='0'+b
    if len(c)<2:
        c='0'+c
    return a+':'+b+':'+c
def solution(play_time, adv_time, logs):
    answer = 0
    Max_length=time_to_num(play_time) #만약 10분이면: 길이가0부터 600까지니까 601이어야함
    length=time_to_num(adv_time)
    
    DP=[0]*(2+Max_length) #누적합 인덱스는 10분이면 0~601임
    for i in logs:
        a,b=map(time_to_num,i.split('-'))
        DP[a]+=1
        DP[b]-=1
    for i in range(1,Max_length+1):
        DP[i]+=DP[i-1]

    
    #answer=sum(DP[:length]) #인덱스 [0:9) LEN=10
    answer=sum( DP[:length] )
    now=answer
    idx=0
    for i in range(1,Max_length-length+1):
        now+=-DP[i-1]+DP[i+length-1] #[1:10)
        if now>answer:
            answer=now
            idx=i
    print(answer)
    print(num_to_time(answer))
    
    return num_to_time(idx)

#print(solution(	"50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
