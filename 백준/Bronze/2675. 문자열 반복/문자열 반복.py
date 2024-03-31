s = int(input())
for i in range(s):
    a = input().split()
    r = int(a[0])
    b = a[1]
    k = 0
    p = ''
    while True:
        try:
            p += b[k]*r
            k+=1
        except:
            break
    print(p)