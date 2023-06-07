import sys
input = sys.stdin.readline

n = int(input())
RGB = list(map(int, input().split()))

for _ in range(n-1):
    r, g, b = map(int, input().split())

    RGB =  [min(RGB[1], RGB[2]) + r,
            min(RGB[0], RGB[2]) + g,
            min(RGB[0], RGB[1]) + b]
print(min(RGB))