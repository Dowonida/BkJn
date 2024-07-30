def solution(cap, n, deliveries, pickups):
    answer = 0
    # 가장 멀리 있는 것 부터 처리한다.
    
    didx = n
    pidx = n
    
    while didx+pidx:
        if didx> pidx:
            
            # deliver의 idx를 최대한 낮추는 방향
            # cnt = 왕복 횟수 if cap==4 : 0->0, 1,2,3,4->1, 5,6,7,8->2
            cnt = (deliveries[didx-1]+cap-1)//cap 
            answer += cnt*2*didx
            rest = cnt*cap-deliveries[didx-1]
            didx -= 1
            while rest and didx:
                additional_deliver = min(rest,deliveries[didx-1])
                rest -= additional_deliver
                deliveries[didx-1] -= additional_deliver
                if not deliveries[didx-1] and didx:
                    didx -= 1
            
            rest = cnt*cap
            while rest and pidx:
                additional_pickup = min(rest,pickups[pidx-1])
                rest -= additional_pickup
                pickups[pidx-1] -= additional_pickup
                if not pickups[pidx-1] and pidx:
                    pidx -= 1
            
            pass
        else:#if pidx>didx:
            # pickups의 idx를 최대한 낮추는 방향
            cnt = (pickups[pidx-1]+cap-1)//cap 
            answer += cnt*2*pidx
            rest = cnt*cap-pickups[pidx-1]
            pidx -= 1
            while rest and pidx:
                additional_pickup = min(rest,pickups[pidx-1])
                rest -= additional_pickup
                pickups[pidx-1] -= additional_pickup
                if not pickups[pidx-1] and pidx:
                    pidx -= 1
            
            rest = cnt*cap
            while rest and didx:
                additional_deliver = min(rest,deliveries[didx-1])
                rest -= additional_deliver
                deliveries[didx-1] -= additional_deliver
                if not deliveries[didx-1] and didx:
                    didx -= 1
        # else:
        #     # idx가 같으면 개수가 더 많은 쪽으로 
        #     pass
        pass

    return answer