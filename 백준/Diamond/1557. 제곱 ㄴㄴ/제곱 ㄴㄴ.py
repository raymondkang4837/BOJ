import math

MX_SZ = 1 << 20
mbs = [0] * MX_SZ

def snn(n):
    p = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        p += mbs[i] * (n // (i * i))
    return p

l = 0
r = 2000000000

k = int(input())

mbs[1] = 1
for i in range(1, MX_SZ):
    if mbs[i]:
        for j in range(i * 2, MX_SZ, i):
            mbs[j] -= mbs[i]

while l < r - 1:
    mid = (l + r) // 2
    if snn(mid) < k:
        l = mid
    else:
        r = mid

print(r)

