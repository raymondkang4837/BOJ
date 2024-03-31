x = { "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0}
up = 0.0
down= 0.0
for i in range(20):
    a, b, c = input().split() #과목 3.0 등급
    if c != "P":
        b = float(b)
        up += b * x[c]
        down += b
print(up / down)