str = input().rstrip();n = len(str);k = 0

for i in range(n):
    if i < n//2:
        k += int(str[i])
    else:
        k -= int(str[i])
        
print("LUCKY" if k==0 else "READY")