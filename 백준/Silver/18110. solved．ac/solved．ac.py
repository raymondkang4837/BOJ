import sys
input = sys.stdin.readline

n = int(input())
if n==0:
    print(n)
else:
    nums = []
    for i in range(n):
        nums.append(int(input()))
    p = n *0.15
    p-int(p)
    if p-int(p) >= 0.5:
        p = int(p) + 1
    else:
        p = int(p)
    nums.sort()
    nums = nums[p:n-p:]
    k = sum(nums)/len(nums)
    if k-int(k) >= 0.5:
        print(int(k) + 1)
    else:
        print(int(k))
