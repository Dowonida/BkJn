class yoseb:
    def __init__(self,num,prev=None,nxt=None):
        self.prev=prev
        self.next=nxt
        self.num=num

    def kill(self):
        self.prev.next=self.next
        self.next.prev=self.prev
        return self.num


N,M=map(int,input().split())
L=[yoseb(1)]
for i in range(2,N+1):
    L.append(yoseb(i,prev=L[-1]))
    L[i-2].next=L[i-1]
L[N-1].next=L[0]
L[0].prev=L[N-1]

def kill(start,M):
    for i in range(M):
        start=start.next
    return start.kill()

D=L[-1]
RST=[]
for i in range(N):
    a=kill(D,M)
 
    RST.append(a)
    D=L[a-1]
    


print("<",end='')
for i in range(N-1):
    print(RST[i],end=', ')
print(RST[-1],end='>')
