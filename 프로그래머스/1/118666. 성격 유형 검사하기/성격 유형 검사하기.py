def solution(survey, choices):
    N     = len(survey)
    typ   = ['TR','FC','MJ','NA']
    score = [0.5,0.5,0.5,0.5] # 동점일 경우 사전순으로 앞서는 점수를 주기 때문에
                              # 조건문 하드코딩을 하지 않기 위해 기본 값을 0.5로 주었다.
                              # RT/CF/JM/AN 유형을 나타낸다.
    dic = {typ[i][j] : i*4+j for i in range(4) for j in range(2)}
    for i in range(N):
        score[dic[survey[i][0]]//4] += ((-1)**(dic[survey[i][0]]%2)) * (choices[i]-4)
    answer = ''.join([typ[i][score[i]>0] for i in range(4)])
    return answer


'''

'''