n, m = map(int, input().split())
coins =[]
for i in range(n):
  coins.append(int(input()))
  
d = [0] * 10001
d[0] = 0
inf = 987654321

for i in range(1, m+1):
  d[i] = inf
  for coin in coins:
    if i >= coin:
      d[i] = min(d[i],  i // coin + d[i % coin])

if d[i] == inf: d[i] = -1
print(d[i])