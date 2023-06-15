import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

arr = list(map(int, ('0 '+input()).rstrip().split()))
for i in range(1,len(arr)):
    arr[i] = arr[i] + arr[i-1]

for i in range(M):
    a, b = map(int, input().rstrip().split())
    print(arr[b] - arr[a-1])