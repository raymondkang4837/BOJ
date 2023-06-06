N = int(input())

# n 개의 숫자들
nums = list(map(int, input().split()))
#덧셈, 뺄셈, 곱셈, 나눗셈의 개수
sam = list(map(int, input().split()))
ans = [0]*N
A = set()
ans[0] = nums[0]

def calculus(x):
    if x == N-1:
        A.add(ans[x])
        return
    for i in range(4):
        if sam[i] == 0:
            continue
        if i==0: # 덧셈
            ans[x+1] = ans[x] + nums[x+1]
            sam[i] -= 1
            calculus(x+1)
            sam[i] += 1
        elif i ==1: # 뺄셈
            ans[x+1] = ans[x] - nums[x+1]
            sam[i] -= 1
            calculus(x+1)
            sam[i] += 1
        elif i==2: # 곱셈
            ans[x+1] = ans[x] * nums[x+1]
            sam[i] -= 1
            calculus(x+1)
            sam[i] += 1
        elif i==3: # 나눗셈
            if ans[x] >=0:
                ans[x+1] = ans[x] // nums[x+1]
                sam[i] -= 1
                calculus(x+1)
                sam[i] += 1
            else:
                ans[x+1] = -(-ans[x] // nums[x+1])
                sam[i] -= 1
                calculus(x+1)
                sam[i] += 1
calculus(0)
print(max(A),min(A),sep='\n')