import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

# dp 테이블 초기화
dp = [[1,1]for _ in range(n)]
dp_set = set()

for i in range(1,n): # i=4
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i][0] = max(dp[j][0]+1, dp[i][0])

for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j] < arr[i]:
            dp[i][1] = max(dp[j][1]+1, dp[i][1])

for num in dp:
    dp_set.add(sum(num))

print(max(dp_set)-1)