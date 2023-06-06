import sys
input = sys.stdin.readline

def f(a,b,c):
    m = str(a)+'.'+str(b)+'.'+str(c)

    if m in memory: #메모리에 값이 있을경우
        return memory[m]
    
    if a<=0 or b <=0 or c<=0:
        memory[m] = 1 # 기억해요~
        return 1
    elif a>20 or b>20 or c>20:
        return f(20, 20, 20)
    
    elif a<b and b<c:
        memory[m] = f(a, b, c-1) + f(a, b-1, c-1) - f(a,b-1, c)
    else:
        memory[m] = f(a-1, b, c) + f(a-1, b-1, c) + f(a-1, b, c-1) - f(a-1, b-1, c-1)
    return memory[m]
    
memory = dict()
memory['0.0.0'] = 1
memory['20.20.20'] = 1048576

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a,b,c,f(a,b,c)))