import sys
input = sys.stdin.readline

n = int(input())
nums = [1] * 10
nums[0] = 0

for _ in range(n-1):
	nums = [
	    nums[1], nums[0]+nums[2], nums[1]+nums[3], nums[2]+nums[4], nums[3]+nums[5],
	    nums[4]+nums[6], nums[5]+nums[7], nums[6]+nums[8], nums[7]+nums[9], nums[8]]
print(sum(nums)%1000000000)