import sys
import math
input = sys.stdin.readline

# 소수 판별 함수
def prime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n %i ==0:
            return False
    return True

for _ in range(int(input())):
    a = int(input())
    
    while prime(a) is False:
        a += 1
    print(a)