import sys
input = sys.stdin.readline

def pre(a):
    print(a, end='')
    if dic[a][0]!='.':
        pre(dic[a][0])
    if dic[a][1]!='.':
        pre(dic[a][1])

def ino(a):
    
    if dic[a][0]!='.':
        ino(dic[a][0])
    print(a, end='')
    if dic[a][1]!='.':
        ino(dic[a][1])

def post(a):
    if dic[a][0]!='.':
        post(dic[a][0])
    
    if dic[a][1]!='.':
        post(dic[a][1]) 
    print(a, end='')

    
N = int(input())

root="A"
dic={}
for i in range(N):
    a,b,c=input().strip().split()
    dic[a]=[b,c]

pre("A")
print()
ino("A")
print()
post("A")
