pos = input()

x = ord(pos[0]) - 96
y = int(pos[1])

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

count = 0

for i in range(8):
  if ((x + dx[i] <= 8) and (x + dx[i] >= 1)):
    if ((y + dy[i] <= 8) and (y + dy[i] >= 1)):
      count += 1
      
print(count)
  