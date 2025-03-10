import sys
input = sys.stdin.readline

# Beakjoon 2836
n, m = map(int, input().split())
nums = []

for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        nums.append((x,-1))
        nums.append((y,+1))

nums.sort()

ans = 0
pos = 0
w = 0

for a,b in nums:
    w += b

    if pos == 0:
        pos = a
    elif w == 0:
        ans += a - pos
        pos = 0
print(m + 2 * ans )