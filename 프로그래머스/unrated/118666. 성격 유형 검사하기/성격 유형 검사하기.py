def solution(survey, choices):
    answer = ''
    dic={'RT':0, 'CF':0, 'JM':0, 'AN':0}
    N=len(survey)
    for i in range(N):
        a=survey[i]
        cnt=-1
        if a[0]>a[1]:
            a=a[::-1]
            cnt=1
        dic[a]+=cnt*(choices[i]-4)
    
    for i in dic:
        if dic[i]>=0:
            answer+=i[0]
        else:
            answer+=i[1]
    return answer