import heapq
def solution(nodeinfo):
    N = len(nodeinfo)
    new_nodeinfo = sorted( [tuple(nodeinfo[i]+[i+1]) for i in range(N)], key=lambda x: -x[1])
    answer = new_nodeinfo
    heap={}
    
    heap[1] = new_nodeinfo[0]
    for i in range(1,N):
        #x만 보면 됨
        cur_key = 1
        info = new_nodeinfo[i]
        while cur_key in heap:
            if info[0]>heap[cur_key][0]:
                cur_key = cur_key*2 + 1
            else:
                cur_key *= 2
        heap[cur_key] = info
    #트리 생성 끝
    
    
    
    visited = {i:0 for i in heap}
    stk = [1]
    visited[1] = 1
    pre_ord = [1] #우선은 키 기준으로 가자
    
    while stk:
        cur = stk[-1]
        if cur*2 in heap and not visited[cur*2]:
            visited[cur*2] = 1
            stk.append(cur*2)
            pre_ord.append(cur*2)
        elif cur*2+1 in heap and not visited[cur*2+1]:
            visited[cur*2+1] = 1
            stk.append(cur*2+1)
            pre_ord.append(cur*2+1)
        else:
            
            stk.pop()
    
    
    stk = [1]
    post_ord = []
    
    visited[1]=2
    while stk:
        
        cur = stk[-1]
        if cur*2 in heap and visited[cur*2]==1:
            visited[cur*2] = 2
            stk.append(cur*2)
              
        elif cur*2+1 in heap and visited[cur*2+1]==1:
            visited[cur*2+1] = 2
            stk.append(cur*2+1)
        else:
            
            post_ord.append(stk.pop())
    
    pre_ord = [heap[i][2] for i in pre_ord]
    post_ord = [heap[i][2] for i in post_ord]
    return pre_ord, post_ord