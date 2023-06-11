import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

x = a * d + b * c
y = b * d

i = x
j = y
if x < y:
    x, y = y, x

while y > 0:
    x, y = y, x%y

print(int(i/x),int(j/x))