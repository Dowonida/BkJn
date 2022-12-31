N, K = map(int,input().split())


#7,2를 생각해보면
#1,2,3,4,5,6,7 중 2번째 2
#1,3,4,5,6,7 중 3번째인 4
#1,3,5,6,7 중 4번째인 6
#1,3,5,7 중 5번째->1번째인 1
#3,5,7 중 2번째인 5
#3,7 중 3번째 -> 1번째인 3
#7 중 2번째 ->


size = 1
while size<1+N:
    size*=2

seg = [0]*size*2

for i in range(size+1,size+1+N):
    seg[i] = 1

for i in range(size-1,0,-1):
    seg[i] = seg[i*2]+seg[i*2+1]


find = 1
K -= 1
rst = []

for i in range(N):
    find += K
    find%=seg[1]
    if find == 0:
        find += seg[1]
    idx = find
    pos = 1
    while pos<size:
        seg[pos]-=1
        if seg[pos*2]>=idx:
            pos*=2
        else:
            idx -= seg[pos*2]
            pos = pos*2+1
    seg[pos] -= 1
    #print(pos-size)
    #print(seg)
    #rst += str(pos-size)+', '
    rst.append(pos-size)
print("<",end='')
for i in range(len(rst)-1):
    print(str(rst[i])+', ',end='')
print(str(rst[-1])+'>')
