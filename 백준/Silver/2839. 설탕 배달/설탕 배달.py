N = int(input())
k = 0
while True:
    if (N - k) % 5 == 0:
        print((N-k)//5 + k//3)
        break
    else:
        k += 3
        if N < k:
            print(-1)
            break