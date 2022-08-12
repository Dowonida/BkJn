import sys
input=sys.stdin.readline

L=list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
D={L[i]:i for i in range(36)}
def _13(n):#10->36
   rst=''
   if n==0:
      return 0
   while n:
      rst=L[n%36]+rst
      n//=36
   return rst
   
def _31(STR): #36->10
   rst=0
   for i in range(len(STR)):
      rst+=D[STR[-1-i]]*(36**i)
   return rst

dic={ L[i]:0 for i in range(36)}
rst=0
N=int(input())
for i in range(N):
   a=input().strip().upper()
   rst+=_31(a)
   for j in range(len(a)):
      C=a[-1-j]
      dic[C]+=(35-D[C])*(36**j)
K=int(input())
V=list(dic.values())
V.sort(reverse=True)
for i in range(K):
   rst+=V[i]
print(_13(rst))
