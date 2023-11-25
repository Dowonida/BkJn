def solution(numbers):
    answer = 0
    count = [0]*10
    for i in numbers:
        count[int(i)] += 1
        
        
    prime = []
    num = [0]*10000000
    for i in range(2,10000000):
        if num[i] == 0:
            num[i] = i
            prime.append(i)
            i_count = [0]*10
            for j in str(i):
                i_count[int(j)] += 1
                if i_count[int(j)] > count[int(j)]:
                    break
            else:
                answer += 1
                
        for j in prime:
            if i*j>=10000000:
                break
            num[i*j] = j
            if i%j == 0:
                break

    return answer