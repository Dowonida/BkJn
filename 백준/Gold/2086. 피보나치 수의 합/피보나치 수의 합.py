'''
a_n까지의 합을 Sn이라고 하자.
그럼 S_(n+1) = Sn+a_(n+1)이고
a_(n+1) = a_n + a_(n-1) = (Sn-S_(n-1)) + (S_(n-1)-S_(n-2)) = S_n - S_(n-2)이다.
따라서 S_(n+1) = 2*S_n - S_(n-2)이다.

이를 행렬로 나타내어 거듭제곱을  해보면
(S_n, -S_(n-2), -S_(n-1))을 (S_k, S_(k-1), S_(k-2))와 내적하면
S_(n+k)가 나오는 것을 알 수 있다. (직접 행렬을 만들어서 거듭제곱해보자.)
따라서 S_k, S_(k-1), S_(k-2)를 가지고 있으면 2배씩 뛰어갈 수 있다.

하지만, S_(k-1), S_(k-2)도 n칸 전진시키기 위해서는
S_(k-3), S_(k-4)도 필요하다.

따라서 S_k, S_(k-1),S_(k-2)를 가지고, S_(k-3), S_(k-4)도 구할 수 있어야 한다.
이는 최초의 식인 S_(n+1) = 2*S_n - S_(n-2)로부터 구해낼 수 있다.

S_(k) = 2*S_(k-1) - S_(k-3)
S_(k-3) = 2*S_(k-1)-S_(k)
S_(k-4)는 위의 식에서 인덱스만 하나씩 내리기 

'''

dic = {-2:0, -1:0, 0:1, 1:2, 2:4}
div = 1000000000


a,b = map(int,input().split())

N = b.bit_length()

def jump(a0,a1,a2,n):
    a3 = 2*a1-a0

    b0 = dic[n]
    b1 = dic[n-1]
    b2 = dic[n-2]
    b3 = 2*b1-b0

    return ((a0*b0-a2*b1-a1*b2)%div,
            (a0*b1-a2*b2-a1*b3)%div,
            (a1*b1-a3*b2-a2*b3)%div)
    

for i in range(2,N):
    n = 1<<i

    idx = n//2
    a0, a1, a2 = dic[idx], dic[idx-1], dic[idx-2]
    dic[n], dic[n-1], dic[n-2] = jump(a0,a1,a2,idx)


def get(n):
    if n in dic and n-1 in dic and n-2 in dic:
        return dic[n], dic[n-1], dic[n-2]

    max_bit = (n.bit_length()-1)
    J = 1<<max_bit
    a0, a1, a2 = get(n- J)
    return jump(a0,a1,a2,J)


B = get(b)[1]
A = get(a)[2]
print((B-A)%div)
