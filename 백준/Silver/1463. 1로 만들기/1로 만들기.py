import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

dp[1] = 0

for i in range(2,n+1):
    p = i%6
    if p == 1 or p == 5:
        dp[i] = dp[i-1] + 1
    elif p == 2 or p == 4:
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    elif p== 3:
        dp[i] = min(dp[i-1], dp[i//3]) + 1
    else:
        dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
    
print(dp[n])