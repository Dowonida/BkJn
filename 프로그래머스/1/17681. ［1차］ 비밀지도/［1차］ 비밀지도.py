def solution(n, arr1, arr2):
    arr3 = [arr1[i]|arr2[i] for i in range(n)]
    answer = [''.join('#' if arr3[i]&(1<<j) else ' ' for j in range(n-1,-1,-1))  for i in range(n)]
    
    return answer