N = int(input())
plans = list(input().split())
x = 1
y = 1

for plan in plans:
  if (plan == 'L'):
    y -= 1
  elif (plan == 'R'):
    y += 1
  elif (plan == 'U'):
    x -= 1
  elif (plan == 'D'):
    x += 1
  
  if (x > N): x = N
  elif (x < 1): x = 1
  if (y > N): y = N
  elif (y < 1): y = 1

print(x, y)