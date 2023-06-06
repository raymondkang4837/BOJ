n = int(input())

ans = 0
row = [0] * n

def test(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def k(x):
    if x < n:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if test(x):
                k(x+1)
    else:
        global ans
        ans += 1
        return
k(0)
print(ans)