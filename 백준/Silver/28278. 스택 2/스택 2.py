import sys
input = sys.stdin.readline
nums = []

for _ in range(int(input())):
    
  var = input().split()

  if var[0] == '1':
    nums.append(var[1])
    
  elif var[0] == '2':
    if nums:
      print(nums.pop())
    else:
      print(-1)
    
  elif var[0] == '3':
    print(len(nums))
    
  elif var[0] == '4':
    if nums:
      print(0)
    else:
      print(1)
    
  elif var[0] == '5':
    if nums:
      print(nums[-1])
    else:
      print(-1)