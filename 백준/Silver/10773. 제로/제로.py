import sys
input = sys.stdin.readline

n = int(input())

pos = 0
stack = [0] * n

for _ in range(n):
    x = int(input())
    if x != 0:
        stack[pos] = x
        pos += 1
    else:
        stack[pos-1] = 0
        pos -= 1
        
print(sum(stack))