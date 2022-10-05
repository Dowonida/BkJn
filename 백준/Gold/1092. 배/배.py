import bisect
M= int(input())
C= list(map(int,input().split()))

N= int(input())
L= list(map(int,input().split()))

C.sort()
L.sort(reverse=True)


if L[0]>C[-1]:
    print(-1)

else:
    AC=[0]*M
    for i in L:
        left=bisect.bisect_left(C,i)
        idx=bisect.bisect_right(AC,AC[left])-1
        AC[idx]+=1
    print(max(AC))
        

    
