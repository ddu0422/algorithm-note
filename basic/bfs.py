from collections import deque


# 정점과 간선이 주어지는 경우
def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()

        for v in graph[now]:
            queue.append(v)
            visited[v] = True


# 이차원 배열이 주어지는 경우
# (4 방향)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# (8 방향)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(graph, x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < row and 0 <= ny < column):
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
