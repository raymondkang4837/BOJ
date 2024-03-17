import sys
input = sys.stdin.readline

n = int(input())
nums = [input() for _ in range(n)]

def paper(nums,n):
    cnt = 0
    for i in nums:
        cnt += i.count('1')
    if cnt == n**2:
        print(1,end='')
        return
    elif cnt == 0:
        print(0,end='')
        return
    print('(',end='')
    paper([nums[i][:n//2] for i in range(n//2)],n//2)
    paper([nums[i][n//2:] for i in range(n//2)],n//2)
    paper([nums[i][:n//2] for i in range(n//2,n)],n//2)
    paper([nums[i][n//2:] for i in range(n//2,n)],n//2)
    print(')',end='')
paper(nums,n)
