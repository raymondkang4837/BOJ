import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def flab(x,y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    cases = 0
    for p in pos:
        xx = x + p[0]
        yy = y + p[1]
        if (0 <= xx < M) and (0 <= yy < N) and (maps[x][y] > maps[xx][yy]):
            cases += flab(xx,yy)
    
    dp[x][y] = cases
    return dp[x][y]

M,N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
dp = [ [-1] * N for _ in range(M) ]
pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]

print(flab(0,0))