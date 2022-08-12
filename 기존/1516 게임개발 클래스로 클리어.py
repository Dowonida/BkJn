import sys
input=sys.stdin.readline
class nod:
    def __init__(self,bt,prev):#bt는 빌드타임, args는 선행건물들
        self.bt=bt
        self.prev=prev
        self.BT=0

    def build(self):
        pretime=0
        for i in self.prev:
            if Nod[i].BT==0:
                Nod[i].build()
            pretime=max(pretime,Nod[i].BT)
        self.BT=pretime+self.bt
        

N=int(input())
Nod=[0]
for i in range(1,N+1):
    a=list(map(int,input().split()))[:-1]
    Nod.append(nod(a[0],a[1:]))
    
for i in Nod[1:]:
    i.build()
    print(i.BT)
