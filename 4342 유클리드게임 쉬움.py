import sys
input=sys.stdin.readline

while True:
    winner='A'
    loser='B'
    a,b=map(int,input().split())
    if (a,b)==(0,0):
        break
    if a==b:
        print(winner,'wins')
        continue
    a,b=min(a,b),max(a,b)
    while True:
        if b//a>1:
            break
        a,b=b%a,a
        winner,loser=loser,winner
    print(winner,'wins')
