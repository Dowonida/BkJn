from heapq import heappop, heappush

N, K = map(int,input().split())

L = list(map(int,input().split()))
current = []

dic = [ [] for _ in range(K+1)]
idx = [ 0 for _ in range(K+1) ]

for i in range(K):
    dic[L[i]].append(i)

for i in dic:
    i.append(1000000)

rst = 0
S = set()
for i in L:
    idx[i] += 1 #다음 인덱스로 넣어줘야함
        #heappush(current, (- dic[i][idx[i]],i))
    if len(S)<N or i in S:
        heappush(current, (- dic[i][idx[i]],i))

        S.add(i)

    else:
        rst += 1
        while True:
            d,p = heappop(current)
            if p in S:
                S.remove(p)
                break
        S.add(i)
        heappush(current, (- dic[i][idx[i]],i))


    #print(S,i,current)
        


print(rst)
