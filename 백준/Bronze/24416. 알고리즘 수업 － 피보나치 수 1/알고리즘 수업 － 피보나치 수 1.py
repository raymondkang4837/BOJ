# 24416
cnt_1 = 0
cnt_2 = 0



# 피보나치 수 재귀호출 의사 코드
def fibo_1(n):
    global cnt_1
    cnt_1 += 1
    if n ==1 or n ==2:
        return 1
    else:
        return fibo_1(n-1) + fibo_1(n-2)
    
# 피보나치 수 동적 프로그래밍 의사 코드
def fibo_2(n):
    k = [0] * (n+1)
    if n ==1 or n==2:
        return 1
    else:
        k[1], k[2] = 1, 1
        for i in range(2,n):
            k[0] += 1
            k[i] = k[i-1] + k[i-2]
        return k[0]

n = int(input())
print(fibo_1(n), fibo_2(n))
