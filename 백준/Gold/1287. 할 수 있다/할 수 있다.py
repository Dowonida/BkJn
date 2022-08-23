dic={"+":1, "-":1, "*":2, "/":2}
M=list(input())
stack=[]
flag=1 #숫자가 들어오면 0 괄호가 열리면, 기호들어오면 1 1인 상태에서 부호 들어오면 ROCK
sick=[]
cnt=1

#ROCK1: 연속숫자
#ROCK2: 괄호가 너무 많이 닫힘
#ROCK3: 기호가 연속으로 옴
#ROCK4: 0으로 나눔
#ROCK5: 숫자가 전부 연산되지 않고 남음
#ROCK6: 닫히지 않은 괄호 존재

#나누기를 //로 했는가?
#괄호닫고나서 숫자오면? 
for i in M:
    if i.isdigit():#숫자면
        if flag==3: #숫자가 연속인 경우
            print("ROCK")
            break
        elif flag==0:
            sick[-1]=int(str(sick[-1])+i)
        else:
            sick.append(int(i))
            flag=0

    elif i=="(":#이 다음에는 숫자가 와야함 즉 기호취급
        flag=1
        cnt*=10
 
    elif i==")": #이 다음에는 기호가 와야함 즉 숫자취급
        flag=3
        cnt//=10
        if cnt<1:
            print("ROCK")
            break

    else:
        
        if flag==1: #기호가 연속으로 온 경우
            print("ROCK")
            break
        else:
            flag=1
            prio=dic[i]*cnt
            while stack and stack[-1][1]>=prio:
                if len(sick)<2:
                    print("ROCK")
                    break


                R=sick.pop()
                L=sick.pop()
                C=stack.pop()[0]

                if C=="+":
                    sick.append(L+R)
                elif C=="-":
                    sick.append(L-R)
                elif C=='*':
                    sick.append(L*R)
                elif C=='/':
                    if R==0:
                        print("ROCK")
                        break
                    else:
                        sick.append(L//R)
            stack.append((i,prio))

else:
    while stack:
        if len(sick)<2:#숫자가 부족한 경우 ex 2-3-
            print("ROCK")
            break
        R=sick.pop()
        L=sick.pop()
        C=stack.pop()[0]

        if C=="+":
            sick.append(L+R)
        elif C=="-":
            sick.append(L-R)
        elif C=='*':
            sick.append(L*R)
        elif C=='/':
            if R==0:
                print("ROCK")
                break
            else:
                sick.append(L//R)
    else:
        if len(sick)!=1:#숫자가 남음
            print("ROCK")
        elif cnt!=1:#괄호가 전부 닫히지 않음
            print("ROCK")
        else:
            print(sick[0])


