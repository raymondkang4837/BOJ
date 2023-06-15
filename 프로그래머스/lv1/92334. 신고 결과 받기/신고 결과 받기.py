def solution(id_list, report, k):
    ans = [0] * len(id_list)
    mail={i:[] for i in id_list}
    
    for i in report:
        a,b = i.split()
        if a in mail[b] or a==b or (b not in id_list):
            continue
        mail[b].append(a)
    
    for i in mail:
        if len(mail[i]) >= k:
            for j in mail[i]:
                ans[id_list.index(j)] += 1
    return ans