import sys
input=sys.stdin.readline


RST=[]
STK=[(0,1e7,1e7)]
while True:
    try:
        a=int(input())
        
        while not(STK[-1][0]<a<STK[-1][2]):
            RST.append(STK.pop()[1])
        if a>STK[-1][1]:
            STK.append((STK[-1][1],a,STK[-1][2]))
        else:
            STK.append((STK[-1][0],a,STK[-1][1]))
            
        
    except:
        break
while len(STK)>1:
    RST.append(STK.pop()[1])
for i in RST:
    print(i)