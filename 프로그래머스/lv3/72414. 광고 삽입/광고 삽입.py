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
    Max_length=time_to_num(play_time) 
    length=time_to_num(adv_time)
    DP=[0]*(2+Max_length) 
    for i in logs:
        a,b=map(time_to_num,i.split('-'))
        DP[a]+=1
        DP[b]-=1
    for i in range(1,Max_length+1):
        DP[i]+=DP[i-1]
    answer=sum( DP[:length] )
    now=answer
    idx=0
    for i in range(1,Max_length-length+1):
        now+=-DP[i-1]+DP[i+length-1] #[1:10)
        if now>answer:
            answer=now
            idx=i
    return num_to_time(idx)
