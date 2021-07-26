n, m = list(map(int, input().split()))
money_value = [0] * (n + 1) # 1 ~ n 개
for i in range(1, n + 1):
  money_value[i] = int(input())

d = [-1] * (m + 1) # 0 ~ m 개
d[0] = 0

for i in range(1, n + 1):
  for j in range(money_value[i], m + 1):
    if d[j - money_value[i]] >= 0:
      d[j] = min(d[j], d[j - money_value[i]] + 1)

print(d[m])