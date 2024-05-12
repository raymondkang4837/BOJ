## 백준 7576번

# 1. 초기 세팅
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
que = deque([])
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# - 1이 있는 위치를 큐에 넣는다.
# - 확산 함수를 실행하여 상하좌우를 보고 0이면 카운트 변수와 함께 넣는다.
# - 다 진행 후 0이 있는지 찾고 1이 몇개 인지 찾으면 끝 !


# step 1
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            que.append([i,j])

# step 2
while que:
    i,j = que.popleft()

    for p in range(4):
        if 0 <= i+dx[p] < m and 0 <= j+dy[p] < n:
            if arr[i+dx[p]][j+dy[p]] == 0:
                arr[i+dx[p]][j+dy[p]] = arr[i][j] + 1
                que.append([i+dx[p], j+dy[p]])

# step 3 
exit = 1

for i in arr:
    if 0 in i:
        exit = 0
    cnt = max(cnt, max(i))

if exit:
    print(cnt - 1)
else:
    print(-1)