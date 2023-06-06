import sys
from collections import deque
input=sys.stdin.readline

def DFS(v):
    # 현재 노드를 방문 처리하기
    visit[v] = True
    print(v,end=' ')
 
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visit[i]:
            DFS(i)

def BFS(v):
    # 큐 구현
    que = deque([v])

    # 현재 노드 방문처리
    visit[v] = True

    # 큐가 빌 때까지 반복
    while que:
        p = que.popleft()
        print(p, end=' ')
        for i in graph[p]:
            if not visit[i]:
                que.append(i)
                visit[i] = True 

N, M, S = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
P = 1 
while P <= N:
    graph[P].sort()
    P += 1

visit = [False] * (N+1)



DFS(S)
print()
visit = [False] * (N+1)
BFS(S)