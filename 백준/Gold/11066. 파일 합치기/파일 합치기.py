import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    data = int(input())
    nums = list(map(int, input().split()))
    dp = [[0 for _ in range(data)] for _ in range(data)]
    
    for gap in range(1,data):
        for start in range(data-gap):
            end = start + gap
            dp[start][end] = 999999999
            s = sum(nums[start:end+1])
            for k in range(start,end):
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + s)
    print(dp[0][data-1])