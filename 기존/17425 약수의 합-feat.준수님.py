import sys
#1~100까지 약수의 합에서 1은 100번나오고
#2는 100//2=50번나오고... 반복
T=int(sys.stdin.readline())

for test_case in range(T):
    L=int(sys.stdin.readline())
    rst=0
    for i in range(1,L+1):
        rst+=(L//i)*i
    print(rst)