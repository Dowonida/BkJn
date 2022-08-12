import sys
input=sys.stdin.readline

N=int(input())
dic={}
for i in range(N):
    a=int(input())
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1
rst=max(dic.values()) #공차가 0 인 수열의 최대 길이
                        #이를 제외하면 나머지는 모든 항이 다른 수열임 

dic=list(dic)
dic.sort()


for i in range(len(dic)-rst):
    cdgc=(dic[-1]-dic[i])//rst #최대공차는 최대차이/수열길이 
    for j in range(i+1,len(dic)):
        d=dic[j]-dic[i]
        if d>cdgc:
            break
        cnt=1
        k=dic[j]
        while k in dic:
            cnt+=1
            k+=d
        if cnt>rst:
            rst=cnt
print(rst)
