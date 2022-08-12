import sys
input=sys.stdin.readline
"""전략 수립
+가 시계방향, -가 반시계 방향(해당면 볼 때 기준)
            123     윗면
            456     
            789     31      41     
11   123    123     123     123    
     456    456     456     456     
     789    789     789     789    
            123     
            456     
            789     61
"""

color=["w","g","r","b","o","y"]
C={ 10*i+j:color[i] for i in range(6) for j in range(1,10)}
Index={"U":0, "L":1, "F":2, "R":3, "B":4, "D":5}
def mainrotate(SB):
    S,B=SB[0],SB[1]
    s=Index[S]
    if B=="+":
        (C[10*s+1],C[10*s+2],C[10*s+3],C[10*s+4],C[10*s+5],C[10*s+6],C[10*s+7],C[10*s+8],C[10*s+9],)=(C[10*s+k] for k in (7,4,1,8,5,2,9,6,3))
    elif B=="-":
        (C[10*s+7],C[10*s+4],C[10*s+1],C[10*s+8],C[10*s+5],C[10*s+2],C[10*s+9],C[10*s+6],C[10*s+3],)=(C[10*s+k] for k in range(1,10))

def siderotate(L,B):
    if B=="+":#리스트를 시계방향으로 입력 43,42,41....13,12,11
        return L[-3:]+L[:-3]
    else:
        return L[3:]+L[:3]

def rotate(SB):
    S,B=SB[0],SB[1]
    mainrotate(SB)
    if S=="U":
        L=(C[43],C[42],C[41],C[33],C[32],C[31],C[23],C[22],C[21],C[13],C[12],C[11])
        (C[43],C[42],C[41],C[33],C[32],C[31],C[23],C[22],C[21],C[13],C[12],C[11])=siderotate(L,B)
    elif S=="D":
        L=(C[17],C[18],C[19],C[27],C[28],C[29],C[37],C[38],C[39],C[47],C[48],C[49])
        (C[17],C[18],C[19],C[27],C[28],C[29],C[37],C[38],C[39],C[47],C[48],C[49])=siderotate(L,B)
    elif S=="L":
        L=(C[1],C[4],C[7],C[21],C[24],C[27],C[51],C[54],C[57],C[49],C[46],C[43])
        (C[1],C[4],C[7],C[21],C[24],C[27],C[51],C[54],C[57],C[49],C[46],C[43])=siderotate(L,B)
    elif S=="F":
        L=(C[7],C[8],C[9],C[31],C[34],C[37],C[53],C[52],C[51],C[19],C[16],C[13])
        (C[7],C[8],C[9],C[31],C[34],C[37],C[53],C[52],C[51],C[19],C[16],C[13])=siderotate(L,B)
    elif S=="B":
        L=(C[39],C[36],C[33],C[3],C[2],C[1],C[11],C[14],C[17],C[57],C[58],C[59])
        (C[39],C[36],C[33],C[3],C[2],C[1],C[11],C[14],C[17],C[57],C[58],C[59])=siderotate(L,B)
    elif S=="R":
        L=(C[59],C[56],C[53],C[29],C[26],C[23],C[9],C[6],C[3],C[41],C[44],C[47])
        (C[59],C[56],C[53],C[29],C[26],C[23],C[9],C[6],C[3],C[41],C[44],C[47])=siderotate(L,B)


def PP():
    print(C[1]+C[2]+C[3])
    print(C[4]+C[5]+C[6])
    print(C[7]+C[8]+C[9])

NN=int(input())
for i in range(NN):
    C={ 10*i+j:color[i] for i in range(6) for j in range(1,10)}
    MM=int(input())
    A=input().split()
    for j in A:
        rotate(j)
    PP()
