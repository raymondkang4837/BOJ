import sys
input = sys.stdin.readline

dogam = {}

n = input()

for i in map(int, input().split()):
    if i not in dogam:
        dogam[i] = 1
    else:
        dogam[i] += 1

m = input()

for i in map(int, input().split()):
    if i in dogam:
        print(dogam[i], end=' ')
    else:
        print(0, end=' ')