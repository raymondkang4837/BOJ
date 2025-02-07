import sys
input = sys.stdin.readline

n = int(input()) # 행렬의 개수
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for gap in range(1,n):
    if gap == 1:
        for i in range(n-1):
            dp[i][i+1] = lst[i][0] * lst[i][1] * lst[i+1][1]
        continue
    for start in range(n-gap):
        end = start + gap
        dp[start][end]  = 2**31
        for k in range(start,end):
            memo = lst[start][0]*lst[k][1]*lst[end][1]
            dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + memo)
            
print(dp[0][n-1])