import sys
input = sys.stdin.readline


def func(before_str, cur_idx):
    if cur_idx == N-1:
        if before_str<L[cur_idx][0]:
            return '0'
        elif before_str<L[cur_idx][1]:
            return '1'
        else:
            return None
    
    
    
    if (before_str<L[cur_idx][0]):
        rst1 = func(L[cur_idx][0], cur_idx+1)
        if rst1 != None:
            return '0' + rst1

    if (before_str<L[cur_idx][1]):
        rst2 = func(L[cur_idx][1], cur_idx+1)
        if rst2 != None:
            return '1' + rst2

    return None
    
rst = []
for _ in range(int(input())):
    N = int(input())
    L = []
    for _ in range(N):
        a = input().strip()
        L.append((a,a[::-1]))
    rst.append(func('',0))
print('\n'.join(rst))
