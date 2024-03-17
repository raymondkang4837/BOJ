n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def paper(nums,n):
    global white, blue
    cnt = 0
    for i in nums:
        cnt += sum(i)
    if cnt == n**2:
        blue += 1
        return
    elif cnt == 0:
        white +=1
        return
    lst1 = [nums[i][:n//2] for i in range(n//2)]
    cnt = 0
    for i in lst1:
        cnt += sum(i)
    if cnt == 0:
        white += 1
    elif cnt == (n**2)//4:
        blue += 1
    else:
        paper(lst1,n//2)
    lst2 = [nums[i][n//2:] for i in range(n//2)]
    cnt = 0
    for i in lst2:
        cnt += sum(i)
    if cnt == 0:
        white += 1
    elif cnt == (n**2)//4:
        blue += 1
    else:
        paper(lst2,n//2)
    lst3 = [nums[i][:n//2] for i in range(n//2,n)]
    cnt = 0
    for i in lst3:
        cnt += sum(i)
    if cnt == 0:
        white += 1
    elif cnt == (n**2)//4:
        blue += 1
    else:
        paper(lst3,n//2)
    lst4 = [nums[i][n//2:] for i in range(n//2,n)]
    cnt = 0
    for i in lst4:
        cnt += sum(i)
    if cnt == 0:
        white += 1
    elif cnt == (n**2)//4:
        blue += 1
    else:
        paper(lst4,n//2)
paper(nums,n)
print(white)
print(blue)