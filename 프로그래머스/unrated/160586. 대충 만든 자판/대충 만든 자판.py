def solution(keymap, targets):
    tap = {}
    for str in keymap:
        p = 1
        for s in str:
            try: # 값이 있는 경우
                tap[s] = min(tap[s], p)
            except : # 값이 없는 경우
                tap[s] = p
            p += 1
    
    answer = []
    for str in targets:
        try:
            n = 0
            for s in str:
                n +=tap[s]
            answer.append(n)
        except:
            answer.append(-1)
        
    return answer