prio={'*':2, '/':2, '+':1, '-':1}
rst=''
stack=[]
cnt=1
for i in input():
    if i=="(":
        cnt*=10
    elif i==")":
        cnt//=10

    elif i in '+-*/':
        if not stack or cnt*prio[i]>stack[-1][1]:
            stack.append((i,cnt*prio[i]))
        else:
            while stack and stack[-1][1]>=cnt*prio[i]:
                rst+=stack.pop()[0]
            stack.append((i,cnt*prio[i]))
    else:
        rst+=i
while stack:
    rst+=stack.pop()[0]
print(rst)
    

