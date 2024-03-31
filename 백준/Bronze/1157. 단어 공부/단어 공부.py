words = input().upper()
solo = list(set(words))
c = []
for x in solo:
    r = words.count(x)
    c.append(r)
if c.count(max(c)) > 1:
    print('?')
else:
    print(solo[c.index(max(c))])