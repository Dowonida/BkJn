def solution(board, skill):
    R = len(board)
    C = len(board[0])
    acum= [[0]*(C+1) for i in range(R+1)]
    for type, rs,cs, re,ce, degree in skill:
        if type==1:
            degree*=-1
        acum[rs][cs]+=degree
        acum[rs][ce+1]-=degree
        acum[re+1][cs]-=degree
        acum[re+1][ce+1]+=degree
    for i in range(R+1):
        for j in range(1,C+1):
            acum[i][j]+=acum[i][j-1]
    for j in range(C+1):
        for i in range(1,R+1):
            acum[i][j]+=acum[i-1][j]
    answer=0
    for i in range(R):
        for j in range(C):
            if acum[i][j]+board[i][j]>0:
                answer+=1
            
    return answer