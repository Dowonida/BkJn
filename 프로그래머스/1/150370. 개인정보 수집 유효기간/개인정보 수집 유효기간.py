def solution(today, terms, privacies):
    def numbering(date):
        y,m,d = date.split('.')
        rst = int(y)*12*28+int(m)*28+int(d)
        return rst
    def due_day(num_date,term):
        return numbering(num_date)+28*term
    
    def main(priv):
        a,b = priv.split()
        return due_day(a, dic[b])
    
    dic = {}
    for i in terms:
        a,b = i.split()
        dic[a] = int(b)
    answer = []    
    
    today = numbering(today)
    print(dic)
    for i, d in enumerate(privacies,1):
        if main(d)<=today:
            answer.append(i)
    
    return answer