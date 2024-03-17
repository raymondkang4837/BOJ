def factoreal(n):
    if n<=1:
        return 1
    else:
        return n*factoreal(n-1)
    
print(factoreal(int(input())))