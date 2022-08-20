N, K= map(int,input().split())


stack=[]
count=0
pos=0
L=input()


while pos<N:
    if stack and count<K and stack[-1]<L[pos]:
        count+=1
        stack.pop()
    else:
        stack.append(L[pos])
        pos+=1

for i in range(K-count):
    stack.pop()
    
for i in stack:
    print(i,end='')
    
