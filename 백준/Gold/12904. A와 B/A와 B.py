before = input()
rbefore = before[::-1]
after = input()

lenA = len(after)
lenB = len(before)

# 시작인덱스를 i라고하면 끝나는 인덱스는 i+lenB가 된다.(i+lenB 미포함)
# 왼쪽에 있는 B의 개수는 L[i-1]이 되고
# 오른쪽에 있는 B의 개수는 numB-L[i+lenB-1]이 된다.

# 정방이면 좌우 B개수가 같고, 시작점 왼쪽에 A가 있으면 안됨
# 역방이면 우측 B가 1개 많고, 도착점 오른쪽에 A가 있으면 안됨

# 즉 체크 순서는 기본은 슬라이싱 윈도우
# 슬라이싱 결과 B개수가 맞으면 A여부 확인 (빠른 커트를 먼저해야함)
# A여부 통과하면 알맹이가 before와 일치하는지

# 우측 B가 더 많아지기 시작하면 체크포인트이므로
# 시작은 우측부터 역순 접근이 좋음

rst = 0

leftB = after[:-lenB].count("B")
rightB = 0
sidx = lenA-lenB
eidx = lenA-1

while leftB>rightB:
    rightB += bool(after[eidx]=='B')
    sidx -= 1
    eidx -= 1
    leftB -= bool(after[sidx]=='B')
    

while leftB+2>rightB and sidx>=0:
    
    if leftB == rightB: # 정방향
        if sidx==0 or after[sidx-1]=="B": #A여부 통과
            if after[sidx:eidx+1] == before:
                rst = 1
                break
    elif leftB+1 == rightB:
        if eidx==lenA-1 or after[eidx+1]=="B": #A여부 통과
            if after[sidx:eidx+1] == rbefore:
                rst = 1
                break

    rightB += bool(after[eidx]=='B')
    sidx -= 1
    eidx -= 1
    leftB -= bool(after[sidx]=='B')
print(rst)
