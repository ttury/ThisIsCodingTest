from collections import deque

n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]

for i in range(n):
  board[i] = list(map(int, list(input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([(0, 0)])
while(queue):
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (nx >= 0 and nx < n and ny >= 0 and ny < m):
      if (board[nx][ny] == 1):
        queue.append((nx, ny))
        board[nx][ny] = board[x][y] + 1

print(board[-1][-1])