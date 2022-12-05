import sys
input = sys.stdin.readline

R, C = map(int,input().split())
mapping = {'.':0,'x':-1}
Map= [[-1]*C] + [
    list(map(lambda x: mapping[x],input().strip())) for _ in range(R)
    ] + [[-1]*C]


rst = 0
for i in range(1,1+R):
    Map[i][0] = 1
    cur_r = i
    cur_c = 0
    stk = [(cur_r,cur_c)]
    while stk:
        cur_r, cur_c = stk.pop()
        Map[cur_r][cur_c] = i
        if cur_c == C-1:
            rst += 1
            break
        for j in range(1,-2,-1):
            next_r, next_c = cur_r+j, cur_c+1
            if Map[next_r][next_c]==0:
                stk.append((next_r,next_c))
                
print(rst)
