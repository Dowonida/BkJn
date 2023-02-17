import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int,input().split()))
#전체 최대, 왼포최대, 오포최대, 전체합
#전체최대 = max(왼전체최대,오전체최대,왼오포최대+오왼포최대)
#왼포최대 = max(왼왼포최대, 왼전체합+오왼포최대)
#오포최대 = max(오오포최대, 오전체합+왼오포최대)
#전체합 = 전체합+전체합

MIN = -100000000
NN= 128*1024
seg = [ [MIN]*4 for _ in range(2*NN)]

for i in range(N):
    seg[i+NN] = [L[i]]*4

for i in range(NN-1,0,-1):
    left = seg[i*2]
    right = seg[i*2+1]
    seg[i] = [max(left[0],right[0],left[2]+right[1]),
              max(left[1],left[3]+right[1]),
              max(right[2],right[3]+left[2]),
              left[3]+right[3]
                ]

for _ in range(int(input())):
    s,e = map(int,input().split())
    s += NN-1
    e += NN

    left = [MIN]*4
    right2 = [MIN]*4
    while s<e:
        if s%2:
            right = seg[s]
            s += 1
            left = [max(left[0],right[0],left[2]+right[1]),
              max(left[1],left[3]+right[1]),
              max(right[2],right[3]+left[2]),
              left[3]+right[3]
                ]
        if e%2:
            e -= 1
            left2 = seg[e]
            right2 = [max(left2[0],right2[0],left2[2]+right2[1]),
              max(left2[1],left2[3]+right2[1]),
              max(right2[2],right2[3]+left2[2]),
              left2[3]+right2[3]
                ]
            
        

        s //= 2
        e //= 2
    
    print(max(left[0],right2[0],left[2]+right2[1]))
