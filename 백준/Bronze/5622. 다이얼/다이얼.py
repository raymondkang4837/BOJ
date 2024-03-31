a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
t = 0
for x in input():
    for k in a:
        if x in k:
            t += a.index(k)+3
print(t)