import sys
input = sys.stdin.readline

n = int(input())

stack, ans = [], [] # 스택과 대응되는 push, pop
find = True # 스택 수열 판정 변수

# 4 3 5 2 6 1
# 1 2 5 3 4
now = 1
for _ in range(n):
    num = int(input())

    # 스택 쌓기
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1

    # 스택 빼기
    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    # 고장난 연산
    else:
        find = False

# 정답 출력
if not find:
    print("NO")
else:
    for i in ans:
        print(i)