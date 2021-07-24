x = int(input())

d = [0] * 30001

d[1] = 0
d[2] = 1

inf = 987654321

for n in range(3, x + 1):
  data1 = d[n-1]
  if n % 2 == 0:
    data2 = d[n//2]
  else:
    data2 = inf
  if n % 3 == 0:
    data3 = d[n//3]
  else:
    data3 = inf
  if n % 5 == 0:
    data4 = d[n//5]
  else:
    data4 = inf
  d[n] = min(data1, data2, data3, data4) + 1

print(d[x])