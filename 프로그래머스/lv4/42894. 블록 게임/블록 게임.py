def solution(board):


    answer = 0
    N=len(board)
    #visited=[[0]*len(board[0]) for i in range(len(board))]
    diff= True
    while diff:
        diff=False
        for r in range(N):
            for c in range(N):
                if board[r][c]!=0:
                    visited={(r,c)}
                    stack=[(r,c)]
                    left,right,top,bot=c,c,r,r
                    block=board[r][c]
                    while stack:
                        nr,nc=stack.pop()
                        left,right,top,bot=min(nc,left),max(nc,right),min(top,nr),max(bot,nr)
                        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nnr,nnc=nr+dr,nc+dc
                            if 0<=nnr<N and 0<=nnc<N and board[nnr][nnc]==block and (nnr,nnc) not in visited:
                                visited.add((nnr,nnc))
                                stack.append((nnr,nnc))
                    #print(left,right,top,bot,block)
                    if board[bot][left:right+1].count(block)!=right-left+1:
                        continue
                    flag=True
                    for i in range(left,right+1):
                        if board[bot-1][i]==block:
                            continue
                        cnt=0
                        for j in range(bot-1,-1,-1):
                            if board[j][i] not in (0,block):
                                cnt+=1
                        flag=flag and (not cnt)

                    if flag==True:
                        diff=True
                        answer+=1
                        for rr,cc in visited:
                            board[rr][cc]=0
    print(board)
    return answer

