import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, arr, vst):
    cnt = 1
    que = deque([n])
    vst[i] = 1
    while que:
        v = que.popleft()
        for next in arr[v]:
            if not vst[next]:
                vst[next] = 1
                que.append(next)
                cnt += 1
    return cnt


n, m = map(int, input().rstrip().split())
arr = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    if a == b: # 두 노드가 같을 경우 
        continue
    else:
        arr[b].append(a)

ans = set()
k = 0

for i in range(1,n+1):
    vst = [0] * (n+1)
    c = bfs(i, arr, vst)
    if c > k:
        ans = set()
        ans.add(i)
        k = c
    elif c == k:
        ans.add(i)

print(*ans)
