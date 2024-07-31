def solution(numbers):
    # 전위순회로 바꾸고
    # 인덱스 조회하면 됨
    
    def main(number):
        # 1. 숫자를 2의 거듭제곱-1 크기의 이진법으로 나타낸다.
        #   1-1) 그러기 위해서는 숫자의 이진법 자리수를 알아야 한다.
        #        숫자의 이진법 자리수는 해당 숫자의 bit_length를 사용하면 된다.
        #   1-2) 어떤 수보다 크면서 가장 작은 2의 거듭제곱 -1을 찾는 법
        #        1<<(bit_length)-1을 하면 된다.

        N = number.bit_length()
        NN = (1<<N.bit_length())-1

        # 2. 자리 수가 2^NN -1자리로 맞춰진 이진법으로 변환한 다음 리스트에 저장한다.
        #   2-1) 이진법을 그대로 저장하면 중위 순회로 저장이 된다.
        #   사족) 문제에서 좌우 대칭은 문제가 없으므로 가장 왼쪽을 1의 자리로 보든, 가장 오른쪽을 1의 자리로 보든 상관 없다.

        # 아래의 코드는 2의 0제곱이 가장 왼쪽이므로 가장 왼쪽이 1의 자리가 된다.
        IT = [1 if number&(1<<j) else 0 for j in range(NN)] # Inorder Tree

        # 3. 중위 순회로 저장된 노드를 깊이 순으로 정렬하자.
        #   3-1) 중위 순회를 정렬하는 것은 재귀 함수를 사용하자.
        #   3-2) 포화 이진트리라는 점을 이용하면, 부모노드는 항상 트리의 가운데 있음을 알 수 있다.
        #   3-3) 이를 이용해서 전위 순회를 한다면 항상 가운데 노드를 먼저 처리해주면 된다. 

        PT = [0] # Preorder Tree 초기화 작업
                 # 0을 처음에 넣어둔 이유는 4-2)를 참고
        
        stk = [((NN-1)//2, (NN+1)//4)]
        for cur_idx, cur_dist in stk:
            PT.append(IT[cur_idx])
            if cur_dist == 0:
                continue
            stk.append((cur_idx-cur_dist,cur_dist//2))
            stk.append((cur_idx+cur_dist,cur_dist//2))

        # 4. 자신이 1이면서 부모노드가 0인 경우가 있는지 확인한다.
        #   4-1) 전위순회로 저장한 이진트리의 장점은 my_idx//2 = parent_idx라는 것이다.
        #   4-2) 위의 조건은 루트 노드의 번호가 1이어야 성립한다.
        #   4-3) 부모노드가 없는 루트를 제외하고 다음 노드를 비교하면 된다.

        for i in range(2,NN+1): # 루트노드인 1은 제외
            if PT[i] == 1 and PT[i//2] == 0:
                return 0
        return 1
            

    answer = [main(n) for n in numbers]
    
    
    return answer