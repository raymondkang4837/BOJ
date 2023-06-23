import sys
input = sys.stdin.readline

n = int(input())
fac = 1
ans = 0
for i in range(1,n+1):
    fac *= i
if n <= 4:
    print(0)
else:
    for k in str(fac)[::-1]:
        if k == '0':
            ans += 1
        else:
            print(ans)
            break
        
