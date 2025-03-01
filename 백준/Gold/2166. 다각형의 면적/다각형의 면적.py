import sys
input = sys.stdin.readline

# Shoelace Formula
n = int(input())
x, y = map(int, input().split())
nums = [x,y,x,y]
ans = 0
for i in range(n-1):
    x,y = map(int, input().split())
    ans -= nums.pop() * x - nums.pop() * y
    nums.append(x)
    nums.append(y)

ans += nums[2] * nums[1] - nums[3] * nums[0]
print(abs(ans)/2)