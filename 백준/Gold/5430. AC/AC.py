import sys
input=sys.stdin.readline

T=int(input())

for test_case in range(T):

    oper = input().strip()
    N = int(input())
    if N==0:
        input()
        L=[]
    else:
        L = list(map(int,input().strip('[]\n').split(',')))


    V = True #True면 왼쪽, False면 오른쪽
    n = oper.count("D")
    if n>N:
        print('error')
        continue
    for i in oper:
        if i=="R":
            V= not V

        else:
            if V:
                L.pop(0)
            else:
                L.pop()
    if not V:
        L=L[::-1]
    print(str(L).replace(' ',''))
