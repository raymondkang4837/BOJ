a, b =map(int, input().split()) #현재 시각
c = int(input())
d, e = a+(b+c)//60, (b+c)%60 #총 시간
print(d%24, e)