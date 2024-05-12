## 백준 2667번 풀이

# 1. 입력 처리
import sys
input = sys.stdin.readline

# 2. 초기 세팅
n = int(input())
M = [list(input().rstrip()) for _ in range(n)]
ans = []
cnt = 0

def counting(arr,i,j):
    global cnt

    if arr[i][j] == '1':
        arr[i][j] = '0'
        cnt += 1
    else:
        return
    
    if i==0:
        counting(arr,i+1,j)
    elif i < n-1:
        counting(arr,i-1,j)
        counting(arr,i+1,j)
    else:
        counting(arr,i-1,j)
    
    if j==0:
        counting(arr,i,j+1)
    elif j < n-1:
        counting(arr,i,j+1)
        counting(arr,i,j-1)
    else:
        counting(arr,i,j-1)

# - (1,1) ~ (n,n) 까지 탐색 
# - 1을 찾으면 가구 함수 실행 (상하좌우 가구 수 세기 : 0으로 바꿈) -> 정답 리스트 추가
# - 오름차순 한 줄 출력

for i in range(n):
    for j in range(n):
        counting(M,i,j)
        if cnt >0:
            ans.append(cnt)
        cnt = 0

print(len(ans), *sorted(ans),sep='\n')