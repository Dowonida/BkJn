import sys
#메모리가 충분해보이므로 테스트케이스에서 가장 큰값을 기준으로
#전부 구한 다음 불러오기
T=int(sys.stdin.readline())

for test_case in range(T):
    L=int(sys.stdin.readline())#L은 입력값
    rst=0
    for i in range(1,int(L**(0.5))+1):#단축시행 횟수
        G=L//i#단축시행의 마지막숫자
        rst+=(G*(G+1))//2
    for i in range(1,(L+1)//2+1):
        rst+=max(0,(L//i-int(L**(0.5))))*i
    print(rst)