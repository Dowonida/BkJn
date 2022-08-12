import sys 
input=sys.stdin.readline
ABC=['0','1','2','3','4','5','6','7','8','9',
'A','B','C','D','E','F','G','H','I','J','K',
'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def DEC2T(N):
    if N==0:
        return '0'
    rst=''
    while N:
        rst=ABC[N%36]+rst
        N=(N-N%36)//36
    return rst
def T2DEC(N):

    rst=0
    for i in range(0,len(N)):
        rst+=ABC.index(N[-1-i])*(36**i)
    return rst

dic={ABC[i]:[35-i,0] for i in range(36)} #값을 저장함. 알파벳별로 계수가 몇인지 #이후 높은거순으로 z로 바꿈
#ABC=ABC[10:]#알파벳만 남김 알파벳이 아니라 숫자를 바꾸니까 무의미 

N=int(input())
rst=0
for i in range(N):
    a=input().strip()
    rst+=T2DEC(a)
    for j in range(len(a)):
        dic[a[-1-j]][1]+=(35-ABC.index(a[-1-j]))*36**j#Z로 바꿀때 더해지는 값 
K=min(int(input()),35)
L=sorted(dic, key=lambda x:dic[x][1]*dic[x][0],reverse=True)#높은 값 역순 정렬 
L.remove('Z')
for i in range(K):
    rst+=dic[L[i]][1]
print(DEC2T(rst))
