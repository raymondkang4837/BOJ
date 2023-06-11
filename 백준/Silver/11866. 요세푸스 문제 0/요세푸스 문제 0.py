# 큐(queue) : 선입 선출
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
m = k - 1

que = deque([i for i in range(1,n+1)])
die = []
while len(que) > 0:
    die.append(que[m])
    del que[m]
    m -= 1
    if len(que) != 0:
        m = (m + k) % len(que)
print("<",end='')
print(*die,sep=', ',end='')
print(">")