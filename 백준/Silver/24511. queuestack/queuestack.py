n = int(input())
str1 = input()
str2 = list(map(int, input().split()))
ans = []

for i in range(n):
    if str1[2*i]=='0':
        ans.append(str2[i])

m = int(input())
str3 = list(map(int, input().split()))

ans.reverse()
k = m - len(ans)
if k >0:
  ans += str3[:k]
print(*ans[:m])