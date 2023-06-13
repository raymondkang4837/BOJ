def solution(k, m, score):
    ans = 0
    score.sort()
    n = len(score)
    if m > n:
        return 0
    x = n % m
    box = n // m
    pos = 1
    while pos <= box:
        ans += score[x] * m
        x += m
        pos += 1
    return ans