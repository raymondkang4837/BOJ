import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c = a*b
    while b!=0 :
        a, b = b, a%b
    print(c//a)