def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in skip:
        alpha = alpha.replace(i,'')
    ans = ''
    l = len(alpha)
    for i in s:
        ans += alpha[(alpha.find(i)+index)%l]
    return ans