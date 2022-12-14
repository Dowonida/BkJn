N = '3'+input()
Max = 1000000
#0이면 이전이 1이나 2여야함
#1~6이면 이전이 아무거나 상관은 없음
#이전이 1,2면 더 앞도 더함
#7~9도 이전이 아무거나 상관은 없음
#이전이 1이면 더 앞도 더함

DP = [0]*(len(N))
DP[0] = 1
for i in range(1,len(N)):
    if N[i]=='0':
        if N[i-1] in '12':
            DP[i] += DP[i-2]
        else:
            print(0)
            break
    elif N[i] in '123456':
        DP[i] += DP[i-1]
        if N[i-1] in '12':
            DP[i] += DP[i-2]
    elif N[i] in '789':
        DP[i] += DP[i-1]
        if N[i-1] == '1':
            DP[i] += DP[i-2]
    DP[i]%= Max
else:
    print(DP[-1])
