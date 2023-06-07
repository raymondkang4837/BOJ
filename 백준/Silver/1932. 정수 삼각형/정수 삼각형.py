import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*(n-i) for i in range(n)]

arr[0][0] = int(input())

for i in range(n-1):
    k = list(map(int,input().strip().split()))
    p = 0
    for j in k:
        if p == 0:
            arr[i+1-p][p] = arr[i-p][p] + j
        elif p == i + 1:
            arr[i+1-p][p] = arr[i+1-p][p-1] + j
        else:
            arr[i+1-p][p] = max(arr[i+1-p][p-1], arr[i-p][p]) + j
        p += 1
    if i == n-2:
        mad = [0] * n
        for j in range(n):
            mad[j] = arr[i+1-j][0+j]

if n == 1:
    print(arr[0][0])
else:
    print(max(mad))