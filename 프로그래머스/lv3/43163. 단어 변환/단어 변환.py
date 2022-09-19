num=[26**i for i in range(10)]
def numbering(string):
    cnt=0
    idx=0
    for i in string:
        cnt+=(ord(i)-97)*num[idx]
        idx+=1
    return cnt
def is_neigbor(a,b):#차이가 26의 거듭제곱이면 
    if a==b:
        return False
    diff=abs(a-b)
    for i in num:
        if diff//i<26 and diff%i==0:
            return True
    return False

def solution(begin, target, words):
    N=len(words)
    start=numbering(begin)
    if target not in words:
        return 0
    end=words.index(target)
    endidx=words.index(target)
    List=[ numbering(i) for i in words]
    dic={ i:[j for j in range(N) if is_neigbor(List[i],List[j])] for i in range(N) }
    dic[-1]= [ i for i in range(N) if is_neigbor(start,List[i])]
    answer = 0
    que=[-1]
    visited=[0]*N
    while que:
        nq=[]
        for i in que:
            for j in dic[i]:
                if visited[j]==0:
                    visited[j]=1
                    nq.append(j)
        
        
        que=nq
        answer+=1
        if visited[end]==1:
            break
    
    return answer