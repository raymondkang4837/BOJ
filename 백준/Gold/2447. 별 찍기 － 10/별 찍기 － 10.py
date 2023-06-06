import sys
input = sys.stdin.readline

n = int(input())
arr = [[1 for _ in range(n)] for _ in range(n)]

def star_set(row,col,N):
    if N != 1:
        P = N//3
        for i in range(P,2*P):
            for j in range(P, 2*P):
                arr[col+i][row+j] = 0

        star_set(row,col,P)
        star_set(row+P,col,P)
        star_set(row+2*P,col,P)
        star_set(row,col+P,P)
        star_set(row,col+2*P,P)
        star_set(row+2*P,col+P,P)
        star_set(row+P,col+2*P,P)
        star_set(row+2*P,col+2*P,P)
    
# 함수 실행
star_set(0,0,n)

# 출력 부분
str = [''] * n
for i in range(n):
    for num in arr[i]:
        if num == 1:
            str[i] += '*'
        else:
            str[i] += ' '
    print(str[i])