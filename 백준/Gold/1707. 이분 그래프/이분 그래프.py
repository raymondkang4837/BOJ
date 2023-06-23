import sys
input = sys.stdin.readline
from collections import deque

def two_bfs(n, nums, arr):
    que = deque([n])
    nums[n] = 1
    while que:
        v = que.popleft()
        for j in arr[v]:
            if nums[j] == nums[v] != 0:
                return 0 # 불가능
            elif nums[j] == 3 - nums[v]:
                continue
            nums[j] = 3 - nums[v]
            que.append(j)
    return 1


k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    nums = {i:0 for i in range(1,n+1)}
    arr = [[] for _ in range(n+1)]

    # 간선 등록
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    # 이분 그래프 검사
    test = 0

    for i in range(1,n+1):
        if nums[i] == 0:
            if two_bfs(i,nums,arr) == 0:
                test = 1
                break

    if test == 1:
        print('NO')
    else:
        print('YES')