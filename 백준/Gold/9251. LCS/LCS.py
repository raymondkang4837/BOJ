# LCS problem
import sys 
input = sys.stdin.readline

wd1, wd2 = input().rstrip(), input().rstrip()
l1, l2 = len(wd1), len(wd2)
nums = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < nums[j]:
            cnt = nums[j]
        elif wd1[i] == wd2[j]:
            nums[j] = cnt + 1
print(max(nums))

