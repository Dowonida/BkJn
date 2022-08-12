import sys
sys.setrecursionlimit(10000000)
'''
odd place에 홀수개,
even place에 나머지를 넣으면 됨
우선 red N개를 배치했다고 치면 자리는 전부 N+1개가 된다.
그 중 반 +1은 짝수개
반은 홀수개임
그러니까 (N+1)//2개가 odd자리 N+1-(N+1)//2가 even자리임

'''
Com={}
def comb(n,r):
    r = min(r, n-r)
    if r<2:
        return n**r
    else:
        if (n,r) in Com:
            return Com[(n,r)]
        else:
            Com[(n,r)] = (comb(n-1,r) + comb(n-1,r-1))%1000000007
            return Com[(n,r)]
N = int(input())
odd_place = (N+1)//2
even_place = N+1 - odd_place

rst=0
odd_num=1
while odd_num<=N:
    even_num = N-odd_num
    rst += comb(odd_place-1+odd_num,odd_num)*comb(even_place-1+even_num,even_num)
    rst %= 1000000007
    odd_num+=2


print(rst)
'''
1   1
2   2
3   10
4   32
5   126
6   452
7   1716
8   6400
9   24310
10  92252
11  352716
12  1351616
13  5200300
14  20056584
15  77558760



'''