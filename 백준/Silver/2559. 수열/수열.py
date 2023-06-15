N, K = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))
nums = [0] * (N-K+1)
for i in range(1, N-K+1):
    nums[i] = arr[K+i-1] - arr[i-1]
for j in range(1, len(nums)):
    nums[j] += nums[j-1]
l = nums.index(max(nums))
print(sum(arr[l:l+K]))