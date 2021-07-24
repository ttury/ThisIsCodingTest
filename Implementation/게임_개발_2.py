N, M = map(int, input().split())
x, y, d = map(int, input().split())

board = [[0] * M for _ in range(N)]

for row in range(N):
  board[row] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

fail_count = 0
count = 1

board[x][y] = 2

while(True):
  if (fail_count == 4):
    nx = x - dx[d]
    ny = y - dy[d]
    if (nx >= 0 and nx < N and ny >= 0 and ny < M):
      if (board[nx][ny] != 1):
        print('clear')
        x = nx
        y = ny
        fail_count = 0
        continue
    break
  
  print(x, y)
  
  d -= 1
  if (d == -1):  d = 3
  nx = x + dx[d]
  ny = y + dy[d]
  
  if (nx >= 0 and nx < N and ny >= 0 and ny < M):
    if (board[nx][ny] == 0):
      print('detect')
      x = nx
      y = ny
      board[x][y] = 2
      count += 1
      fail_count = 0
    else:
      fail_count += 1
  else:
    fail_count += 1
    
print(count)