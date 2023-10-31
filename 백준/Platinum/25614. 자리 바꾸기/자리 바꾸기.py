import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dic = {}
L = list(map(int,input().split()))
RST = [-1]*(N)
for i in range(N):
    if RST[i] != -1:
        continue #이미 배정 받음

    my_set = [i+1]
    cur = L[i]
    while cur!=i+1:
        my_set.append(cur)
        cur = L[cur-1]

    Len = len(my_set)
    if Len in dic:
        MM = dic[Len]
    else:
        MM = M%Len
        dic[Len] = MM
    for start_index in range(Len):
        end_index = (MM)%Len
        RST[my_set[start_index]-1] = str(my_set[end_index])
        MM += 1


print(' '.join(RST))
