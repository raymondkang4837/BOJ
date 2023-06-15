def solution(survey, choices):
    test = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey, choices):
        if A not in test:
            A = A[::-1]
            test[A] -= B-4
        else:
            test[A] += B-4
    
    ans = ''
    for i in test:
        if test[i] > 0:
            ans += i[1]
        elif test[i] < 0:
            ans += i[0]
        else:
            ans += sorted(i)[0]

    return ans