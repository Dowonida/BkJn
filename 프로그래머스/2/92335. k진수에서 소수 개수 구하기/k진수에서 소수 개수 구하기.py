##1번만 틀림
MM=10000000#여기 있는 소수로만 안나눠지면 어차피 소수
L=[0]*(MM)
prime=[]
for i in range(2,MM):
    if L[i]==0:
        if '0' not in str(i):
            prime.append(i)
        for j in range(i,MM,i):
            L[j]=1


def solution(n, k):
    global MM
    answer=0
    rst=''
    
    
    while n:
        rst+=str(n%k)
        n//=k
    rst=rst[::-1].split('0')

    for i in rst:
        if not i or i=='1':
            continue
        for p in prime:
            if p**2>int(i):
                answer+=1
                break
            if int(i)%p==0:
                break
            
    return answer


