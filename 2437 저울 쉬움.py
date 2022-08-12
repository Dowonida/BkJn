N=int(input())
L=list(map(int,input().split()))
L.sort()
rst=0
for i in L:
    if i>rst+1:
        break
    else:
        rst+=i

print(rst+1)
