def solution(k, score):
    top = [score[0]]
    ans = [score[0]]
    if k > len(score):
        k = len(score)
    for i in range(1,k):
        top.append(score[i])
        ans.append(min(score[i], ans[-1]))
    
    for i in range(k, len(score)):
        if ans[-1] < score[i]:
            top.append(score[i])
            top.remove(ans[-1])
        ans.append(min(top))
    return ans
