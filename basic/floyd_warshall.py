import sys

INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 양방향이라고 가정
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = cost
    graph[b][a] = cost

# 자기 자신으로 돌아오는 길은 없으므로 0
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y:
            graph[x][y] = 0


# 플로이드 워셜
def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


floyd_warshall()