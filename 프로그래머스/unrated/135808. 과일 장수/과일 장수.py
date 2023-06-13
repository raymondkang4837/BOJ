def solution(k, m, score):
    return sum(sorted(score)[-m::-m])*m