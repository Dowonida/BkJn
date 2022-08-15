N=int(input())
List=list(map(int,input().split()))
List.sort()

L=0
R=N-1
D=List[R]+List[L]
rst=[List[L],List[R],D]
while L<R:
    if abs(D)<abs(rst[2]):
        rst=[List[L],List[R],D]
    if D>0:
        R-=1
    elif D<0:
        L+=1
    else:
        print(List[L],List[R])
        break
    D=List[L]+List[R]
else:
    print(rst[0],rst[1])
