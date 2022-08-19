A=input()
B=list(input())
L=[]
m=len(B)
for n,i in enumerate(A):
    L.append(i)
    if i==B[-1] and L[-m:]==B:
        for j in range(m):
            L.pop()

if L:
    for i in L:
        print(i,end='')
else:
    print("FRULA")
