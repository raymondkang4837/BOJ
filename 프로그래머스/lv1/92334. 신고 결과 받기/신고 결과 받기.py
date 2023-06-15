def solution(id_list, report, k):
    ans = [0] * len(id_list)
    mail={i:[] for i in id_list}
    
    for i in set(report):
        a,b = i.split()
        mail[b].append(a)
    
    for i in mail:
        if len(mail[i]) >= k:
            for j in mail[i]:
                ans[id_list.index(j)] += 1
    return ans