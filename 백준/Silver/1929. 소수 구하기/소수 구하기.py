import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [1] * (m+1)
a[0], a[1] = 0, 0

for i in range(2, m+1):
    if a[i]:
        for j in range(i * 2, m+1,i):
            a[j] = 0
for i,_ in enumerate(a[n:], start=n):
    if _:
        print(i)