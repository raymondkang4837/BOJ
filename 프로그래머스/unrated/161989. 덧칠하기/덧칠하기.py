def solution(n, m, section):
    clean = 0
    cnt = 0
    for i in section:
        if i > clean:
            clean = i + m - 1
            cnt += 1
    return cnt