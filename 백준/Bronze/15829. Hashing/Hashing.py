import sys
input = sys.stdin.readline

n = int(input())
code = input().rstrip()
alpha = 'abcdefghijklmnopqrstuvwxyz'
ans = 0

for i in range(n):
    ans += (alpha.index(code[i])+1) * (31 **i)
print(ans % 1234567891)