def solution(s):
    answer = ''
    S=s.split(' ')
    An=[]
    for j in S:
        a=''
        for i in range(len(j)):
            if i%2:
                a+=j[i].lower()
            else:
                a+=j[i].upper()
        An.append(a)
    
    return ' '.join(An)