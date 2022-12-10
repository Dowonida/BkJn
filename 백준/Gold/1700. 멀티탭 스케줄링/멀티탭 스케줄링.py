N, K = map(int,input().split())

L = list(map(int,input().split()))
current = set()

dic = [ [] for _ in range(K+1)]
idx = [ 0 for _ in range(K+1) ]

for i in range(K):
    dic[L[i]].append(i)

for i in dic:
    i.append(1000)

rst = 0
for i in L:
    if len(current)<N or i in current:
        current.add(i)
        
    else:
        a = max(current, key = lambda x: dic[x][idx[x]])
        current.remove(a)
        current.add(i)
        rst += 1
    idx[i] += 1

print(rst)
