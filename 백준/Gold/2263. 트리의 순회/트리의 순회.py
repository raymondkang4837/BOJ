import sys

#Beakjoon 2263
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
idx = [0] * (n+1)

for i in range(n):
    idx[inorder[i]] = i

def preorder(in_i,in_j,post_i,post_j):
    if in_i > in_j or post_i > post_j:
        return
    root = postorder[post_j]
    print(root, end=' ')
    
    n_left = idx[root] - in_i
    n_right = in_j - idx[root]
    preorder(in_i, in_i + n_left - 1, post_i, post_i + n_left - 1)
    preorder(in_j - n_right + 1, in_j, post_j - n_right, post_j - 1)

preorder(0,n-1,0,n-1)
print()