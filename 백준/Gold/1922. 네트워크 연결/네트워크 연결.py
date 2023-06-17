import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int, input().rstrip().split())) for _ in range(int(input().rstrip()))], key=lambda x : x[2])

'''
최소 스패닝 이론 문제
1. 간선 비용 정렬
2. 낮은 값부터 간선 개설
3. 사이클 함수 돌리기
'''
cost = 0
nums = {i:0 for i in range(1,n+1)}
new = 1

def circle(x,y):
    global new
    if nums[x] == 0 and nums[y] == 0: # 간선이 없는 두 구역
        nums[x], nums[y] = new, new
        new += 1
    elif nums[x] == nums[y]: # 동일한 그룹에 존재하는 두 구역
        return False
    elif nums[x] == 0: # x구역만 간선이 없을 경우
        nums[x] = nums[y]
    elif nums[y] == 0: # y 구역만 간선이 없을 경우
        nums[y] = nums[x]
    else: # 서로 다른 그룹에 있는 구역들 (합치기)
        k = nums[y]
        for i in nums:
            if nums[i] == k:
                nums[i] = nums[x]
    return True

for x in arr:
    if circle(x[0],x[1]) and x[0] != x[1]:
        cost += x[2]
print(cost)