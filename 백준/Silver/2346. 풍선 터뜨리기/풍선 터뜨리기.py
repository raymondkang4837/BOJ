import sys
input = sys.stdin.readline

n = int(input())
nums = [i for i in range(1,n+1)]
arr = list(map(int, input().split()))
i = 0
m = 1

for _ in range(n-1):
    print(nums.pop(i), end= ' ')
    k = arr.pop(i)
    if k>0:
      i += k-1
    else:
      i += k
    i %= n-m
    m += 1
print(nums.pop(i))