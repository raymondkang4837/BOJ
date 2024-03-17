import sys
from collections import deque

input = sys.stdin.readline
lst1 = deque()

def deck(que, s):
    if s[0] == '1':
        que.appendleft(int(s[2:]))
    elif s[0] == '2':
        que.append(int(s[2:]))
    elif s == '3':
        print(que.popleft() if que else -1)
    elif s == '4':
        print(que.pop() if que else -1)
    elif s == '5':
        print(len(que))
    elif s == '6':
        print(0 if que else 1)
    elif s == '7':
        print(que[0] if que else -1)
    elif s == '8':
        print(que[-1] if que else -1)

for i in range(int(input())):
    deck(lst1, input().strip())