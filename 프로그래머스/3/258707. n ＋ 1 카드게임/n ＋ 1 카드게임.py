
def solution(coin, cards):
    n = len(cards)
    N = n+1
    # draw에 짝 없는 카드 추가
    # 1. 카드를 최대한 뽑기
    # 2. pair에서 카드 가져오기
    # 위 작업을 코인이 떨어질 때까지 반복
    # 조건을 따로 걸기 귀찮으니까 엄청 비싼 조커 카드를 추가해두자.
    answer = 1
    hand = set()
    draw = set()
    two_coin = set()
    
    for i in range(n//3):
        card = cards[i]
        if N-card not in hand:
            hand.add(card)
            continue
        answer += 1
    
    for i in range(n//3,n):
        if i == 2*answer + n//3:
            if two_coin and coin>1:
                coin -= 2
                two_coin.pop()
                answer += 1
            else:
                break
        card = cards[i]
        if N-card in hand and coin:
            coin -= 1
            answer += 1
        elif N-card in draw:
            two_coin.add(card)
        else:
            draw.add(card)
        
    
        
    

    return min(n//3+1,answer)


