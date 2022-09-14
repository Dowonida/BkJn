N=input()

answer=1e41
M=[1e41]
def func(N,Max):
    global answer
    if len(Max)>2 and Max[1]>answer:
        return
    if not N:
        answer= min(answer,Max[1])
        return
    for i in range(len(N)):
        if int(N[i:])<Max[-1]:
            func(N[:i],Max+[int(N[i:])])


func(N,M)
print(answer)
