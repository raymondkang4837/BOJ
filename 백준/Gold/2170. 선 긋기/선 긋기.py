import sys
input = sys.stdin.readline

# Beakjoon 2170 
nums = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    nums.append((a,1))
    nums.append((b,-1))

nums.sort()
ans = 0 
pos = 0
w = 0

for x,y in nums:
    if pos == 0:
        pos = x
        w += 1

    else:
        if y == 1:
            w += 1
        else:
            w -= 1
            if w == 0:
                ans += x-pos
                pos = 0
print(ans)
