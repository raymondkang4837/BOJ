import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = a * b
if a > b:
    while b >0:
        a, b = b, a%b
    print(int(c/a))
    
elif a < b:
    a, b = b, a
    while b >0:
        a, b = b, a%b
    print(int(c/a))

else:
    print(a)