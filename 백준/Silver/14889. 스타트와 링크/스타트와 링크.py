# 14889 스타트와 링크
# 1. 팀을 나누기
# 2. 능력치 차이를 구해서 셋에 넣기
# 3. 능력치 차이의 최솟값을 출력할 것

import sys
input = sys.stdin.readline

n = int(input()) # 0 부터 n-1 의 선수 번호 
mat = [list(map(int, input().split())) for _ in range(n)]

# 팀 나누기
nums = []
ans = []

def team(x,y):
    if y == n//2:
        score(nums)
        return
    for i in range(x, n//2+y+1):
        nums.append(i)
        team(i+1,y+1)
        nums.remove(i)

# 점수 측정
def score(nums):
    cnt = 0
    for i in nums:
        for j in nums:
            if i <j:  
                cnt += mat[i][j] + mat[j][i]
    ans.append(cnt)

# 선별 과정 실행
team(0,0)

kkt = set()
for i in range(len(ans)//2):
    kkt.add(abs(ans[i] - ans[-i-1]))
    
print(min(kkt))