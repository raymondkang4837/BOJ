import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

w_list = [0] * (n) 
v_list = [0] * (n)

for i in range(n):
    w_list[i], v_list[i] = map(int, input().rstrip().split()) 

dp = [0] * (k+1) # dp[0] ~ dp[k] 

for i in range(n): #n번 루프를 걸쳐서 마지막 dp값을 찾아보자
    for j in range(k,w_list[i]-1,-1):
        dp[j] = max(dp[j], dp[j-w_list[i]]+v_list[i])

print(dp[k])