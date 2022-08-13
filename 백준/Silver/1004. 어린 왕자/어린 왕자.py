import sys
input=sys.stdin.readline
#도착점, 시작점을 감싸는 원의 번호를 저장한 다음
#대칭차집합해서 개수 구하면 끝


def is_B(p,A):#p는 좌표 튜플 A는 중심과 반지름 튜플
    x,y=p
    X,Y,R=A
    if (X-x)**2+(Y-y)**2<R**2:
        return True
    else:
        return False


T=int(input())
for test_case in range(T):
    set1=set()#출발
    set2=set()#도착
    x1,y1,x2,y2=map(int,input().split())
    p1=(x1,y1)
    p2=(x2,y2)
    N=int(input())
    for i in range(N):
        A=tuple(map(int,input().split()))
        if is_B(p1,A):
            set1.add(i)
        if is_B(p2,A):
            set2.add(i)
    print(len(set1^set2))
