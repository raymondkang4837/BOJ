import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

# 1번 칸의 최대 부분 수열
dp = [1] * n

for i in range(1, n):
    for j in range (0,i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[j]+1, dp[i])

print(n - max(dp))