from collections import deque

N, M = map(int, input().split())

board = [[0] * M for _ in range(N)]
for i in range(N):
  board[i] = list(map(int, list(input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def print_board(board):
  for row in range(len(board)):
    print(board[row])
  print()

def bfs(graph, start, count):
  queue = deque([start])
  x, y = start
  graph[x][y] = 1
  while(queue):
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if (nx >= 0 and nx < N and ny >= 0 and ny < M):
        if (not graph[nx][ny]):
          queue.append((nx, ny))
          graph[nx][ny] = 1
    
count = 0


for i in range(N):
  for j in range(M):
    if (not board[i][j]):
      count += 1
      bfs(board, [i, j], count)
      print_board(board)

print(count)