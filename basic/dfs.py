# 정점과 간선이 주어지는 경우
def dfs(graph, vertex, visited):
    graph[vertex] = True

    for v in graph[vertex]:
        if not visited[graph]:
            dfs(graph, v, visited)


# 이차원 배열이 주어지는 경우
# (4 방향)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# (8 방향)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def dfs(graph, x, y, visited):
    visited[x][y] = True

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < row and 0 <= ny < column):
            continue

        if not visited[nx][ny]:
            dfs(graph, nx, ny, visited)
