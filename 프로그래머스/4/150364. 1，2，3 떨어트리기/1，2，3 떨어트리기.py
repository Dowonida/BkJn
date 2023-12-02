def gcd(a,b):
    a,b = sorted((a,b))
    while a:
        a,b = b%a, a
    return b
def lcm(a,b):
    return (a*b)//gcd(a,b)
def lcm_multi(L):
    rst = 1
    for i in L:
        rst = lcm(rst,i)
    return rst


def solution(edges, target):
    answer = []
    # 형제 노드끼리 최대 3배차 +a(1바퀴만큼 즉 +3)
    # 임의의 형제 노드에 대해서
    # 나보다 앞(형)에 나*3+3 이하의 값만 있어야하고
    # 나보다 뒤(동생)에 나*3 이하의 값만 있어야 한다.
    # 나보다 작은 값에 대해선, 내가 누군가의 큰 값이므로 고려 x
    # depth가 2인 트리를 기준으로 답을 낼 수 있다면
    # 위로 값을 전달해 줄 수 있을 듯
    # 그런데 왼쪽의 답이 여러가지일텐데, 그 중에서 형의 길이가 동생길이보다 1이하로 커야함
    # 만약 깊이가 2인 완전포화이진트리에서 가장 짧은 것만 병합해서 가지고 있을 경우
    # 4,5번에서 길이가 1인거끼리 병합했는데, 5,6번에서 길이가 2인것끼리 병합해버리면
    # 답을 낼 수가 없다.
    # 따라서 가능하다면 4,5에서 길이가 총 길이가 4 또는 5인 결과도 가지고 있어야 한다.
    # 즉 길이에 대한 모든 경우의 수를 가지고 있어야 한다...?
    # 그런데 길이를 가장 짧은 것이나 가장 긴 것만 가지고 있으면 늘리는건 쉬울지도?
    # 3을 1,2 또는 1,1,1로 쪼개주면 되잖아....? 아니면 합치는 방법도 가능은 할 듯
    # 그렇다면 가장 짧은 것을 주는 것이 메모리 측면에서 효율적
    # 그럼 어떻게 쪼개거나 합치지... [1,3,3,3], [3,3]을 합쳐야하는 경우
    # [3,3]을 쪼개야하는데 앞의 3은 왼쪽 자식의 3이고, 뒤의 3은 오른쪽 자식의 3이라면
    # [1,2] + [3]은 가능하지만, [3]+[1,2]는 불가능하다.
    # 즉 [1,3,2]로 쪼개져야한다. (또는 [1,1,2,2] 등으로 쪼갤 수도 있다.)
    # 그런데 이게 또 트리 깊이가 깊어지면 관리를 어떻게 해야하지?
    # 
    # 대신 길이가 같다면 사전순으로 앞서는 것만 주면 된다.
    # 그럼 길이*3+3 규칙은 버려도 된다. 어차피 이 과정에서 답이 나오네
    # (여기서 잠깐. 답에 부합하는 방법을 구하려면 문자열의 사전순이 아닌 숫자의 사전순)
    # (답을 병합하는 방법은 자식들의 답을 앞에서부터 번갈아가며 붙이면 가장 빠른 사전순이 유지된다.)
    # 
    #
    # 각 리프 노드엔 자기 싸이클 번호가 몇 번인지 저장
    # 각 노드엔 자신의 서브트리에서 어느 노드를 쪼갤 차례인지를 저장?
    # ㄴㄴ 그냥 각 노드에 대한 길이를 알면 다음 번호를 찾으면 된다.
    # 찾는 방법은 심플하겐 각 리프노드에 저장된 (n,k)에 대해서 len(p)==k (mod n)을 만족하는 리프노드 찾기
    # 그런데 이걸 빨리 찾는 방법이 있을지가 관건이네
    # 찾았다치면 그 친구의 값 중 쪼갤 수 있는 가장 앞의 값을 쪼개서 넣어주면 됨
    # 그런데..... 맨 뒤에 넣는건 또 문제인게 사전순이 깨지게 된다.
    # target 값은 100이하니까 미루는 작업은 최대 100번이긴 함 할만할지도?
    # 찾는 방법도 100번이긴 함...
    # 그럼 쪼개는 횟수가 도대체 몇번일까?
    # 병합할 때마다 쪼개기 작업이 들어가고
    # 병합은 최대 100번
    # 그럼 100 * (100+100)이네...?
    # 아니지 병합 한번에 자식 노드 개수-1 만큼 쪼개기 해야할 수도 있잖아
    # 뭐 그렇게 쳐도 100만이네
    # 해볼만 할지도??
    # 재귀로 해야 메모리가 나을텐데
    N = len(edges)+1
    p = [0]*(N+1)
    sons = [[] for _ in range(N+1)]
    for a,b in edges:
        sons[a].append(b)
        p[b] = a
    for i in sons:
        i.sort()
    def split(ans):
        target = len(ans['ans'])
        for i in ans['sons']:
            x,y = my_info[i]
            if target%x == y:
                me = i
                break
        sub_ans = ans['ans'][y::x]
        
        rst = []
        for i in range(len(sub_ans)):
            if len(rst) > i or sub_ans[i] == 1:
                rst.append(sub_ans[i])
            else:
                rst.append(1)
                rst.append(sub_ans[i]-1)

        if len(rst) == len(sub_ans):

            ans['ans'] = [-1]
            
            return 1
        
        ans['ans'].append(0)
        print(ans,x,y)
        print(rst)
        print(sub_ans)                
        ans['ans'][y::x] = rst


        
        #return
    
    my_info = [(0,0) for _ in range(N+1)]
    def recur(a):
        # 필요한 값:
        # 자식에 대한 결과
        # 몇 번 리프를 쪼개야하는지
        # 내 밑에 있는 리프 노드들의 순서는 어떤지
        # a = 2
        # rst = {'ans': [3,2], 'cut': 0, 'sons':{4:(2,0), 5:(2,1)}}
        # -> sons는 value는 따로 저장, key만 집합 또는 리스트로 사용
        
        # 해석: 2번 노드까지 처리한 현재 결과는 [3,2]이고, 컷은 0을 잘라야함
        # 컷이 2k+0이면 4번 노드를 자르고, 컷이 2k+1이면 5번 노드를 자른다.
        # 서브트리에 대한 결과는 노드에 저장하지만
        # 전체 결과는 결국 노드별로 리턴해야하니까, 자른 다음에 리프노드에도 반영해주자.
        if not sons[a]:
            ans = []
            if target[a-1]%3:
                ans.append(target[a-1]%3)
            ans += [3]*(target[a-1]//3) 
            my_info[a] = (1,0)
            return {'ans':ans, 'sons' : [a]}
        rst = {'ans':[], 'sons':[]}
        rst_temp = [recur(i) for i in sons[a]]
        
        #불가능 확인 
        for i in rst_temp:
            if i['ans']==[-1]:
                return {'ans':[-1]}
        
        #자식 업데이트
        Len = len(rst_temp)
        max_idx = 0
        for i in range(Len):
            if len(rst_temp[i]['ans']) >= len(rst_temp[max_idx]['ans']):
                max_idx = i

                
        total_len = 0
        for i in range(Len):
            cnt = len(rst_temp[max_idx]['ans'])-len(rst_temp[i]['ans'])
            if i>max_idx:
                cnt -= 1
            for j in range(cnt):
                print(cnt)
                if split(rst_temp[i]):
                    return {'ans':[-1]}
            total_len += len(rst_temp[i]['ans'])
            for j in rst_temp[i]['sons']:
                rst['sons'].append(j)
                a,b = my_info[j]
                my_info[j] = (a*Len,b*Len+i)
        
        ans = [0]*total_len
        
        for i in range(Len):
            ans[i::Len] = rst_temp[i]['ans']
        
        rst['ans'] = ans
                
        return rst
        
        #스플릿
        #가장 개수가 많은 점 중에서 가장 오른쪽이 기준
        #기준으로부터 왼쪽은 기준과 같은 길이로 맞춤
        #기준으로부터 오른쪽은 기준-1로 맞춤
        
                
            
            
        return rst
    rst = recur(1)['ans']
    print(my_info)
    return rst