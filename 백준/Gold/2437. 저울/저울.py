import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split()))) # 저울들의 오름차순 숫자 리스트
ans = 0 # 만들 수 있는 숫자의 최대값

for i in arr:
    if i - ans <= 1: # 변수로 들어온 값이 만들수 있는 범위와 연결이 되어 있다면
        ans += i # 기존의 만들 수 있는 최대에 변수 값을 더한 값까지 다 만들 수 있다는 뜻.
print(ans+1)