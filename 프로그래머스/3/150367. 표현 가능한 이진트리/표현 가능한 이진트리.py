def solution(numbers):
    # 전위순회로 바꾸고
    # 인덱스 조회하면 됨
    32+8+2
    #101010=0101010
    # 0:1
    # 2:1
    # 4:5
    # 6:5
    # 1:3
    # 5:3
    # 로직: 처음엔 0부터 2칸씩, 부모는 왼쪽 1 오른쪽1
    #       그 다음엔 0+1에서 4칸씩 부모는 왼쪽2 오른쪽2
    #       그 다음엔 0+1+2에서 8칸씩 부모는 왼쪽4 오른쪾4
    #   그럼 s=0, cnt=1, flag = +1로 시작, 
    #   싸이클 내에서 flag *=1
    #   싸이클 변경시 s += cnt, cnt *= 2
    #   하나라도 걸리면 아웃
    #   트리 구성은 좌우대칭도 상관없으니 2로 계속 나누자
    def make_tree(n):
        b = n.bit_length()
        bb = b.bit_length()
        tree = ''
        for i in range((1<<bb)-1):
            if (1<<i)&n:
                tree += '1'
            else:
                tree += '0'
        return tree
    def check_ans(tree):
        start_idx = 0
        cnt = 2
        flag = -1
        L = len(tree)
        while start_idx<L//2:
            for i in range(start_idx,L,cnt):
                flag *= -1
                
                if tree[i] > tree[i+flag]:
                    return 0
                    
                
            flag *= 2
            start_idx += cnt//2
            cnt *= 2
            
        return 1
    
    answer = [check_ans(make_tree(n)) for n in numbers]
    return answer