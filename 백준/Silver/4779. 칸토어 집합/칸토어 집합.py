def cantor(start, n):
    if n == 1:
        return
    for i in range(start + n//3, start+ (n//3)*2): # 가운데 문자열을 공백으로
        arr[i] = ' '
    cantor(start, n//3) # 왼쪽 자르기
    cantor(start + n//3 * 2, n//3) # 오른쪽 자르기

while True:
    try:
        N = int(input())
        arr = ['-'] * (3**N)
        cantor(0, 3**N)
        print(''.join(arr))
    except:
        break