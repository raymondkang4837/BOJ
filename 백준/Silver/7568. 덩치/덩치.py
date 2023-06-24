import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) + [0] for i in range(n)]


pos = 0

while pos < n:
    cnt = 1
    x, y = arr[pos][0], arr[pos][1]
    for i in range(n):
        if arr[i][0] > x and arr[i][1] > y:
            cnt += 1
    arr[pos][2] = cnt
    pos += 1

for i in arr:
    print(i[2], end= ' ')