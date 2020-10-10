import sys

# 노드, 간선의 수
n, m = map(int, sys.stdin.readline().rstrip())
parent = [i for i in range(n + 1)]
edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((cost, a, b))

edges.sort()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)