import sys
import heapq

INF = int(1e9)
# 노드의 수, 간선의 수, 시작 노드
n, m, start = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 단방향이라고 가정
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, cost))

# 데이크스트라
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for v, c in graph[now]:
            cost = dist + c

            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))


dijkstra(start)