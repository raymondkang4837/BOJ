import sys

def dp(x):
    if x in temp:
        return temp[x]
    if (x % 3 == 0) and (x % 2 == 0):
        temp[x] = min(dp(x//3)+1, dp(x//2)+1)
    elif x % 3 == 0:
        temp[x] = min(dp(x//3)+1, dp(x-1)+1)
    elif x % 2 == 0:
        temp[x] = min(dp(x//2)+1, dp(x-1)+1)
    else:
        temp[x] = dp(x-1)+1
    return temp[x]
x = int(sys.stdin.readline())
temp = {1:0}
print(dp(x))