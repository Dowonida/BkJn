def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    idx = {id_list[i]:i for i in range(len(id_list))}
    dic = {i:set() for i in id_list}
    for i in report:
        a,b = i.split()
        dic[b].add(a)
    
    for i in dic:
        if len(dic[i])>=k:
            for j in dic[i]:
                answer[idx[j]] += 1
                
    
    return answer