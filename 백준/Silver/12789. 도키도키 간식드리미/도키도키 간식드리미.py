import sys
input = sys.stdin.readline

n = int(input()) # 사람 수

lst1 = list(map(int, input().split()))+[n+2] # 입구
lst1.reverse() 
lst2 = [n+2] # 대기구
exit = 1 # 출구: n+1이 되면 성공!
run = 1

def go_stop(arr):
    global exit
    k = 1
    while k:
        if exit==arr[-1]:
            arr.pop()
            exit += 1
        else:
            k = 0



while run:
    m = lst1.pop()
    if m == exit: #나가는 번호면 나간다.
        exit += 1
    elif m < lst2[-1]:
        lst2.append(m)
    else: #나가는 번호가 아니면 대기줄로
        print('Sad')
        run = 0; break
    go_stop(lst2)

    if exit == n+1:
        print('Nice')
        run = 0