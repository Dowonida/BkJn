def gcd(a,b):
    while a:
        a, b = b%a, a
    return b

N, K = map(int,input().split())#소시지/평론가
N %= K
if N==0:
    print(0)
    
else:
    G = gcd(N, K)
    K //= G
    print((K-1)*G)
    