import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = {input().strip() for _ in range(n)}

count = 0

for _ in range(m):
    if input().strip() in a:
        count += 1
        
print(count)