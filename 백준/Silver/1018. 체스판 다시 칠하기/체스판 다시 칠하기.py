n, m = map(int, input().split()) # n은 세로, m은 가로
A = [] # 표본 체스판
C = [] # 체스판 만들기 위해 바꿔주는 경우 리스트
answer = 0
for _ in range(n):
    A.append(input())
# 이동 변수 만들기
for a in range(0, n-7):
    for b in range(0, m-7):
# 1. WB 체스판 만들기
        for i in range(0+a, 8+a):
            for j in range(0+b, 8+b):
                if (i + j) % 2 == 0 and A[i][j] == "B":
                    answer += 1
                elif (i + j) % 2 == 1 and A[i][j] == "W":
                    answer += 1
        C.append(answer)
        answer = 0
# 2. BW 체스판 만들기
        for i in range(0+a, 8+a):
            for j in range(0+b, 8+b):
                if (i + j) % 2 == 0 and A[i][j] == "W":
                    answer += 1
                elif (i + j) % 2 == 1 and A[i][j] == "B":
                    answer += 1
        C.append(answer)
        answer = 0
print(min(C)) #체크 포인트 2