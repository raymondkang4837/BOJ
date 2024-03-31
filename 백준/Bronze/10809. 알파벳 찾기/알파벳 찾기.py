s = input()
a = 'abcdefghijklmnopqrstuvwxyz'
k = 0
for i in a:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')