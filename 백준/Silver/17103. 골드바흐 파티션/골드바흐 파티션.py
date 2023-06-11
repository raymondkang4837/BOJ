import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
m = max(a)

b = [0] * 2 + [1] * (m-1)

for i in range(2, m//2+1):
    if b[i]:
        for j in range(2*i, m,i):
            b[j] = 0

for num in a:
    x = 0

    for i in range(2, num//2 +1):
        if b[i] and b[num - i]:
            x += 1
    print(x)