import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    d, now = heapq.heappop(q)
    if distance[now] < d:
      continue
    for edge in graph[now]:
      cost = d + edge[1]
      if cost < distance[edge[0]]:
        distance[edge[0]] = cost
        heapq.heappush(q, (cost, edge[0]))
        
dijkstra(start)

for node in range(1, n+1):
  if distance[node] == INF:
    print("INFINITY")
  else:
    print(distance[node])