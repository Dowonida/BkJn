X,Y,D,T=map(int,input().split())

dist=(X*X+Y*Y)**(0.5)
if D/T<1:
    print(dist)

else:
    if dist<D:
        a=T*2
        b=dist
        c=(D-dist%D)+T
        print(min(a,b,c))
    else:
        a=T*(dist//D+bool(dist%D))
        b=dist%D+T*(dist//D)
        c=(D-dist%D)+T*(dist//D+1)
        print(min(a,b,c))
            
''' 
조금이동후 점프 (직선으로만이동)
    목적지방향이동후 점프 
    반대로 이동 후 점프 

            
그냥 계속점프
    대신 점프거리보다 가까우면 사용 불가

그냥 걷기


'''
'''
반경 안에 있는 경우: 2점프
반경 밖에 있는 경우:+1점프 
공통 : 걷고 나머지 점프(반경 안이면 0점프) 뒤로 빼서(D-dist%D) 점프

'''
