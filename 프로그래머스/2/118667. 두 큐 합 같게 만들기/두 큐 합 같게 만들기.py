def solution(queue1, queue2):
    
    '''
    잠깐 그러면 하나의 큐만 써서 슬라이딩 윈도우를 해도 되겠는데?
    작은 큐를 앞에 둬야하나 큰 큐를 앞에 둬야하나?
    뒤의 인덱스를 왼쪽으로 당기는건 중복 계산 가능성이 높아지니까
    작은 큐를 앞에 두자
    
    처음엔 시작 인덱스가 0, 끝 인덱스가 N
    합이 크면 시작 인덱스를 뒤로 밀고
    합이 작으면 끝 인덱스를 뒤로 민다.
    민 횟수를 합치면 결과가 된다.
    즉 return sidx+eidx-N
    '''
    N = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if sum1<sum2:
        que = queue1 + queue2
    else:
        que = queue2 + queue1
    total = sum1+sum2
    cur_sum = min(sum1,sum2)
    
    sidx = 0
    eidx = len(queue1)
    while eidx!=2*N:
        cur_rest = total-cur_sum
        if cur_sum == cur_rest:
            return sidx+eidx-N
        elif cur_sum < cur_rest:
            cur_sum += que[eidx]
            eidx += 1
        else:
            cur_sum -= que[sidx]
            sidx += 1
    
    return -1