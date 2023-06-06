n = int(input())
def hanoi(N,A,B,C):
    if N==1:
        print(A,C)
    else:
        hanoi(N-1,A,C,B)
        print(A,C)
        hanoi(N-1,B,A,C)
print(2**n-1) 
hanoi(n,1,2,3)