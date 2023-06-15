def solution(today, terms, privacies):
    year, month, day = map(int, today.split('.'))
    a = {}
    for i in terms:
        p, q = i.split()
        a[p] = int(q)
    
    b = 1
    ans=[]
    for i in privacies:
        date, t = i.split()
        c = a[t]
        y,m,d = map(int, date.split('.'))
        y = y + (a[t]+m-1)//12
        m = (a[t]+m-1)%12+1
        d -= 1
        if d == 0:
            m -= 1
            d = 28
            if m == 0:
                y -= 1
                m = 12
        if year < y: # 지금 2022년 유통기한 2023
            b += 1
            continue
        elif year == y and month < m: # 2022.04 vs 2022.04
            b += 1
            continue
        elif year == y and month == m and day <= d: #2022.05.24 vs
            b += 1
            continue
        else:
            ans.append(b)
            b += 1
    return ans