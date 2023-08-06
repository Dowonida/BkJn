import sys
input = sys.stdin.readline
'''
정수론
    홀수 k에 대해서,
    연속된 k개 수의 합은 k의 배수이다.
    따라서 짝수만 고려하면 된다. (x<y이므로 1도 포함x)

    짝수 k에 대해서,
    연속된 4개의 수의 합은
    가운데 두 수의 합의 2배이다.
    같은 식으로 k=2n (n>1)인 경우
    연속된 k개의 수의 합은 n의 배수이다.

    결론
    연속된 두 수의 합만 확인하면 된다.
    따라서 100만까지의 소수를 저장하고 2개씩만 보면 된다.

L, R 쿼리에 대하여
    연속된 두 수의 합이 소수인지 판정하는 방법
    L R쿼리를 할 때마다 계산하면 이미 했던 계산을 또 하는 경우가 많을 것이다.
    ex) 2 6쿼리와 3 7 쿼리가 들어오면 3 4 5 6은 두 번 계산하게 된다.
    각 수 n에 대하여 n+(n+1)이 소수인지 아닌지 저장해두면 된다.

    저장하는 방법
    소수를 추가할 때 

    그런데 그러면 L~R을 전부 돌면서 하나씩 확인해봐야 한다.
    이는 세그먼트 트리를 사용하면 될 듯

    세그먼트 트리에 저장하는 방법
    1개의 숫자가 그 자체로 소수라면 L~R을 처리하면 되지만
    2개의 숫자의 합이 소수라면 L~R-1을 처리해야한다.
    따라서 세그먼트 트리의 하나의 자리에 0,1,2처럼 넣을 순 없다.
    그럼 (is_prime, sum_is_prime)식으로 각각 저장할까
    그러면 L~R에 대한 결과를 구한 다음에 seg[R][1]을 빼주면 된다.
    (seg[R][1]에는 R+(R+1)이 소수인지 아닌지가 저장되므로)

    그런데 어차피 R+(R+1)이 있는지는 in set으로 찾으면 되니까
    굳이 튜플로 이중연산하지말고 합으로 하자.
'''

Max = 1024*1024
factor = list(range(Max))
prime = []
half_prime = []
for i in range(2,Max):
    if factor[i] == i:
        prime.append(i)
        half_prime.append(i//2)
    for j in prime:
        k = i*j
        if k>=Max:
            break
        factor[k] = j
        if i%j==0:
            break
prime = set(prime)
half_prime = set(half_prime)

seg = [0]*Max+[ (i in half_prime) for i in range(Max)]
for i in range(Max-1,0,-1):
    seg[i] = seg[2*i]+seg[2*i+1]

for _ in range(int(input())):
    L, R = map(int,input().split())
    s, e = L+Max, R+Max+1
    rst = -(R in half_prime)
    while s<e:
        if s%2:
            rst += seg[s]
            s += 1
        if e%2:
            e -= 1
            rst += seg[e]
        s //= 2
        e //= 2
            
    print(rst)
