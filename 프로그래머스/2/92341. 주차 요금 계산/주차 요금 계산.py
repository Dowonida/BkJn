def solution(fees, records):
    # 문제 요약 - 문제에서 중심적으로 파악해야하는 요소
    # 요금표 : 기본 시간, 기본 요금, 단위 시간, 단위 요금
    # 입/출차 기록: 시각 오름차순
    # OUT이 없는 경우에는 23:59에 OUT 처리
    # -> records에 OUT 23:59를 일괄 적용하여 처리하면 좋다.
    # 중간에 여러번 들어왔다 나가도 기본시간을 안채웠으면 기본요금 1회만 부과된다.
    
    # 로직 계획
    # 모든 시간을 분 단위로 환산
    # 올림 구현 : (num-1)//mod +1
    # IN인 경우 IN 딕셔너리에 차량번호: 들어온 minute 저장
    # OUT인 경우 TIME 딕셔너리에 차량번호: 시간 기록, IN에서 제거
    # records가 끝나면 IN 딕셔너리에 남은 값들에 대해서 23:59 OUT처리
    # -> records에 OUT 23:59 안넣어줘도 되겠다.
    
    def to_min(time):
        a,b = map(int,time.split(':'))
        return a*60+b
    IN = {}
    TIME = {}
    for r in records:
        t, n, s = r.split()
        t = to_min(t)
        if s == 'IN':
            IN[n] = t
            if n not in TIME:
                TIME[n] = 0
        else:
            TIME[n] += t-IN[n]
            del(IN[n])
    end = to_min('23:59')

    for r in IN:
        TIME[r] += end - IN[r]
    
    answer = []
    for n in sorted(TIME):
        answer.append(fees[1]+max(0,fees[3]*((TIME[n]-fees[0]-1)//fees[2]+1)))

    return answer