import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    distance_now, node_now = heapq.heappop(q)
    if distance_now > distance[node_now]:
      continue
    for edge in graph[node_now]:
      cost = distance_now + edge[1]
      if cost < distance[edge[0]]:
        distance[edge[0]] = cost
        heapq.heappush(q, (cost, edge[0]))

dijkstra(start)

count = 0
max_cost = 0
for node in range(1, n + 1):
  if distance[node] != INF:
    count += 1
    max_cost = max(max_cost, distance[node]) 
    
print(count - 1, max_cost)