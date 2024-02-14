def solution(new_id):
    stk = ['.']
    A = set('qwertyuiopasdfghjklzxcvbnm')
    B = set('1234567890_-')
    for i in new_id.lower():
        if i in A:
            stk.append(i)
        elif i in B:
            stk.append(i)
        elif i == '.' and stk[-1]!=i:
            stk.append(i)
    stk = stk[1:16]
    if not stk:
        stk.append('a')
    if stk[-1] == '.':
        stk.pop()
    while len(stk)<3:
        stk.append(stk[-1])
    answer = ''.join(stk)

    return answer