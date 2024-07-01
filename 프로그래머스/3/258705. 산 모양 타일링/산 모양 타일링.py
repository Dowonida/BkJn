def solution(n, tops):
    answer = 0
    # top은 따로 계산을 안해도 된다. top 밑에 있는 삼각형에 의존하기 때문
    # 바닥 삼각형은 두 가지 경우의 수가 있다. 혼자 있거나, 다음과 연결하거나
    # 중간 삼각형은 세 가지 경우의 수가 있다. 혼자 있거나, top과 연결하거나, 다음과 연결하거나
    # 이를 이용해서 DP를 하면 된다.
    # 그런데 중간 삼각형만 고려하는 방법도 있다.
    # 중간 삼각형을 기준으로 혼자, 왼쪽연결, 오른쪽 연결, 위로 연결
    # 이렇게 생각하는 이유는 인풋 자체가 top을 기준으로 주어지기때문에 중간 삼각형을 기준으로 생각하면 개수가 맞춰지기 때문이다.
    # DP[n]은 n번째 중간 삼각형을 [혼자, 좌, 우, 상]연결로 생각해보자.
    # DP[n][0] = sum(DP[n-1])
    # DP[n][1] = DP[n-1][0]+DP[n-1][1]+DP[n-1][3]
    # DP[n][2] = sum(DP[n-1])
    # DP[n][3] = sum(DP[n-1])
    # 그러면 0,2,3의 값이 일치하므로 하나로 취급해도 될듯
    DP = [[0,0,0,0] for _ in tops]
    DP[0] = [1,1,1,tops[0]]
    for i in range(1,len(tops)):
        DP[i][0] = sum(DP[i-1])%10007
        DP[i][1] = DP[i-1][0]+DP[i-1][1]+DP[i-1][3]%10007
        DP[i][2] = sum(DP[i-1])%10007
        DP[i][3] = sum(DP[i-1])*tops[i]%10007
    return sum(DP[-1])%10007