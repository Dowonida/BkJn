def solution(friends, gifts):
    answer = 0
    # adj = {i:{'give':0, 'recieve':0} for i in friends} # key가 value에게 준 횟수
    adj = {i:{i:0 for i in friends+[0]} for i in friends} # 위의 방법은 사람 이름이 give, recieve가 있을 수도 있다.
                                     # 추가로, 준 선물 - 받은 선물 값만 있으면 되므로 하나의 값으로 관리
    answer = {i:0 for i in friends}
    for a,b in map(lambda x: x.split(),gifts):
        adj[a][0] += 1
        adj[b][0] -= 1
        adj[a][b] += 1
    for i in friends:
        for j in friends:
            i_score = (adj[i][j],adj[i][0])
            j_score = (adj[j][i],adj[j][0])
            if i_score > j_score:
                answer[i] += 1
            elif i_score < j_score:
                answer[j] += 1
                
    return max(answer.values())//2