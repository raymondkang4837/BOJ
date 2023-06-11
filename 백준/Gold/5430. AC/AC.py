# 큐(queue) : 선입 선출
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    cmd = input().rstrip()
    n = int(input())
    que = input().rstrip()[1:-1]
    reverse = 0
    error = 0
    if n ==0:
        que = deque([])
    else:
        que = deque(map(int, que.split(',')))
    for i in cmd:
        if i == "R":
            reverse += 1
        else:
            if n == 0 or len(que) == 0:
                error = 1
                break
            elif (reverse % 2) == 0:
                que.popleft()
            else:
                que.pop()
    if error == 1:
        print("error")
    elif (reverse % 2) == 0:
        print("[",end='')
        print(*que, sep=',', end='')
        print(']')
    else:
        que.reverse()
        print("[",end='')
        print(*que, sep=',', end='')
        print(']')