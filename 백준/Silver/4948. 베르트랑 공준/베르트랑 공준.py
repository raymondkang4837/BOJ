import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    a = [0] * 2 + [1] * (2*n-2)

    for i in range(2,2*n):
        if a[i]:
            for j in range(2*i,2*n,i):
                a[j] = 0
    for i in range(n+1):
        a[i] = 0
    if n == 1:
        print(1)
    else:
        print(a.count(1))