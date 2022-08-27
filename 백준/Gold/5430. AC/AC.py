import sys
input=sys.stdin.readline

class deque:
    def __init__(self,List):
        self.val=List
        self.left=0
        self.right=len(List)

    def __repr__(self):
        return '['+','.join(self.val[self.left:self.right])+']'

    def popleft(self):
        self.left+=1
    def pop(self):
        self.right-=1

    def reverse(self):
        self.val=[ self.val[i] for i in range(self.right-1,self.left-1,-1)]
        self.left=0
        self.right=len(self.val)

        

T=int(input())

for test_case in range(T):

    oper = input().strip()
    N = int(input())
    if N==0:
        input()
        L=deque([])
    else:
        L = deque(input().strip('[]\n').split(','))


    V = True #True면 왼쪽, False면 오른쪽
    n = oper.count("D")
    for i in oper:
        if i=="R":
            V= not V

        else:
            if V:
                L.popleft()
            else:
                L.pop()
                
    if L.left>L.right:
        print('error')
    else:
        if not V:
            L.reverse()
        print(L)                
                



