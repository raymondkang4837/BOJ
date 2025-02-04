import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sarr = [0]*(n+1)
rarr = [0] * (m)

for i in range(1,n+1):
    sarr[i] = sarr[i-1] + arr[i]
    rarr[sarr[i]%m] += 1

cnt = rarr[0]

for i in range(m):
    x = rarr[i]
    cnt += x*(x-1)//2

print(cnt)