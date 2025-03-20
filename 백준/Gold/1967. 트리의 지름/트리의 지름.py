import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def visit_dfs(node):
    global ans
    for next, cost in graph[node]:
        if visit[next] == -1:
            visit[next] = visit[node] + cost
            if ans[1] < visit[next]:
                ans = [next, visit[next]]
            visit_dfs(next)

ans = [0,0]
visit = [-1] * (n+1)
visit[1] = 0
visit_dfs(1)
visit = [-1] * (n+1)
visit[ans[0]] = 0
visit_dfs(ans[0])
print(ans[1])
