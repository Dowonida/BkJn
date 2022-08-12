import sys

T=int(sys.stdin.readline())

for test_case in range(T):
    L=int(sys.stdin.readline())#L은 입력값
    rst=L*L
    for i in range(2,L):
        rst-=T%i
    print(rst)