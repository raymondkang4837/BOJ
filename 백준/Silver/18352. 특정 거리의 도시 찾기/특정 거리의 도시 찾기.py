import sys
from collections import deque
input = sys.stdin.readline

# 특정 거리의 도시 찾기
def run(bfs, start, vst, K):
    que = deque([[start, 0]])
    # 방문처리
    vst[start] = False
    n = 1

    while que:
        v = que.popleft()
        
        for i in bfs[v[0]]:
            if vst[i]:
                que.append([i,v[1]+1])
                vst[i] = False
                if v[1] == K-1:
                    ans.append(i)
        if v[1] == K:
            break
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, input().rstrip().split())

# BFS로 풀어보자
bfs = [[] for _ in range(N+1)]
vst = [True for _ in range(N+1)]
ans = []

for i in range(M):
    a, b = map(int, input().split())
    bfs[a].append(b)

run(bfs, X, vst, K)

if ans:
    ans.sort()
    for i in ans:
        print(i)
else:
    print(-1)