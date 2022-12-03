mod = 10007
dic={}

def comb(n,k):
    k = min(k,n-k)
    if k==0:
        return 1
    elif k<0:
        return 0
    elif k==1:
        return n

    if (n,k) in dic:
        return dic[(n,k)]
    dic[(n,k)] = (comb(n-1,k-1)+comb(n-1,k))#%mod
    return dic[(n,k)]

dic2 = {}
def recur(remain,card_idx=13):#13부터 1까지 역순
    if remain<4 or remain>card_idx*4:
        return 0
    if (remain,card_idx) in dic2:
        return dic2[(remain, card_idx)]
    rst = comb(card_idx*4-4,remain-4)# 여기서 4개 뽑음.
    
    for i in range(4):
        rst += comb(4,i)*recur(remain-i, card_idx-1)
    dic2[(remain, card_idx)] = rst
    return dic2[(remain, card_idx)]

        



def main():
    #Max = comb(52,n)
    
    print(recur(int(input()))%mod)

main()
    
