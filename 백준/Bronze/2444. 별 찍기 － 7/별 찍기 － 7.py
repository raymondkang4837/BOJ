a = int(input())-1
b = 2*a-1
for i in range(a+1):
    print(' '*(a-i)+'*'*(2*i+1))
for i in range(1,a+1):
    print(' '*i+'*'*(2*a+1-2*i))
    