import sys
input = sys.stdin.readline
n = int(input())
mat = [1,2]
for _ in range(3,n+1):
    mat[0], mat[1] = mat[1], (mat[0] + mat[1]) % 15746
if n ==1:
    print(1)
else:
    print(mat[1])