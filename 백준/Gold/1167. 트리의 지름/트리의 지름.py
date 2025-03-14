import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

# BeakJoon 1167

input = sys.stdin.readline
n = int(input())
nums = [[] for _ in range(n + 1)]

# Graph
for _ in range(n):
    i = 1
    for x in map(int, input().split()):
        if x == -1 :
            break
        if i == 1:
            p = x
            i = 2
        elif i == 2:
            k = x
            i -= 2
        else:
            nums[p].append((k,x))
            i += 2


# Checking
visited = [-1]*(n+1)
arr = [1]
visited[1] = 0
ans = []

def dfs_cost_checking(node, cost):
    for son, weight in nums[node]:
        total = cost + weight
        if visited[son] == -1: # 끝
            visited[son] = total
            dfs_cost_checking(son, total)

dfs_cost_checking(1,0)
tmp = [0,0]
for i in range(1,len(visited)):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

visited = [-1] * (n+1)
visited[tmp[0]] = 0
dfs_cost_checking(tmp[0],0)

print(max(visited))