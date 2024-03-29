#기본적으로 1,3개를 바탕으로 생각하면 상대가 뭘 가져가도 4개씩 맞춰서 가져갈 수 있다.
#그럼 결국 처음부터 답이 정해져있는 셈이다.
#하지만 4개가져가기를 통해서 턴을 바꿀 수 있다. (4개는 1개가져가기+3개가져가기이므로 홀짝이 바뀌는 셈)
#그렇지만 4개가져가기로 뒤집으면 다시 4개가져가기로 뒤집으면 된다.
#4개가져가기를 4개가져가기로 카운터치는 경우는 8개 이상 남았을 경우에만 되므로
#8개 이상 남은 상황에선 항상 4개씩 서로 카운터를 치게된다.
#따라서 남은 돌이 8개보다 적은 상황만 생각하면 된다.
#즉 유리한 상황을 먼저 세팅한 다음 4를 몇번 수행하는지가 관건 
#1이면 선공, 2이면 후공, 3이면 선공, 4이면 선공, 5이면 선공(311), 6이면 선공 (411), 7이면 후공, 8이면 선공이 이긴다. 라고 생각했는데
'''
1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21
0   1   0   0   0   0   1   0   1   0   0   0   0   1   0   1   0   0   0   0   1
실제로 남은 돌 개수별로 승리플레이어를 적어보면 위와 같다. (0이 선공 또는 해당 돌이 남았을 때 승리)
작성방법은 다음과 같다.
1,3,4일때는 무조건 0이다.
나머지 n에 대해서 n-1,n-3,n-4 중 하나라도 1이 있으면 그걸 상대한테 넘겨주면 된다. (즉 상대는 선공이 지는 게임의 선공이 된다.) 따라서 선공이 승리한다.
n-1,n-3,n-4 전부 선공이 승리한다면 지금 당장게임에선 선공이 패배할 수 밖에 없다. 

만약 1,4,5라면 어떻게 될까?
1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21
0   1   0   0   0   0   0   1   0   1   0   0   0   0   0   1   0   1   0   0   0
8개 단위가 된다.
1,n,n+1이라면 1~n-1까지는 0,1이 반복되다가 n과 n+1에서 0이 나오고 n개의 0이 나온다?


만약 1,5,6이라면?
1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21
0   1   0   1   0   0   0   0   0   0   1   0   1   
'''
N=int(input())
if N%7==2 or N%7==0:
    print("CY")
else:
    print("SK")