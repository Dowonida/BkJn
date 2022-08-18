Num=[]
STR=input()

rst=''
for i in STR:#숫자저장
    if i in ['-','+']:
        Num.append(int(rst))
        rst=''
    else:
        rst+=i
Num.append(int(rst))


for i in range(10):
    STR=STR.replace(str(i),'')
#STR은 부호만 남음
#첫숫자는 무조건 양수임
cnt=0 #부호에선cnt번, Num에선 cnt+1번
#STR[cnt]가 없으면=> cnt==len(STR)

rst=Num[0]
while cnt<len(STR):
    if STR[cnt]=='+':
        rst+=Num[cnt+1]
    else:
        rst-=sum(Num[cnt+1:])
        break
    cnt+=1
    
print(rst)
