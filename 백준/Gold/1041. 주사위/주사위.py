'''3개의 면을 고르는 경우의 수
윗면포함4개, 아랫면포함4개
abc
abd
aec
aed

fbc
fbd
fec
fed


2개의 면 고르기
ab ac ad ae
fb fc fd fe
bc bd ec ed


N=1인 경우 전체합-최댓값

N>1인 경우
3면개수 4개 고정
2면개수 4*(N-1) 기둥개수
        +4*(N-2) 천장개수=4*(2N-3)

1면개수: (N-2)제곱*5+(N-2)*4=(N-2)*(5N-6)


4*6
3*12
1*9

24+36+9


12+216+352
'''


N=int(input())
num = list(map(int,input().split()))

if N==1:
    print( sum(num)-max(num))
else:
    a,b,c=min(num[0],num[5]),min(num[1],num[4]),min(num[2],num[3])
    M=max(a,b,c)
    _3=a+b+c
    _2=_3-M
    _1=min(a,b,c)
    print(_3*4+_2*(4*(2*N-3))+_1*(N-2)*(5*N-6))
