import sys
input=sys.stdin.readline
sys.setrecursionlimit(20000)

def func(L):
    if len(L)<2:
        return L
    a=L[0]
    for i in range(1,len(L)):
        if L[i]>a:
            break
    else:
        i+=1
    return func(L[1:i])+func(L[i:])+[a]


L=[]
while True:
    try:
        L.append(int(input()))
    except:
        break
print(*func(L))

