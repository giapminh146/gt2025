import heapq

def build_weighted_adj_matrix():
    n = 9 
    matrix = [[0] * n for _ in range(n)]

    edges = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]

    for start, end, weight in edges:
        matrix[start - 1][end - 1] = weight
        matrix[end - 1][start - 1] = weight

    return matrix

def prims_algorithm(matrix, start_node):
    size = len(matrix)
    visited = [False] * size
    priority_queue = [(0, start_node, start_node)]
    mst = []
    total_cost = 0

    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue)

        if visited[v]:
            continue

        visited[v] = True

        if u != v:
            mst.append((u + 1, v + 1, weight))
            total_cost += weight

        for neighbor, cost in enumerate(matrix[v]):
            if cost > 0 and not visited[neighbor]:
                heapq.heappush(priority_queue, (cost, v, neighbor))

    return mst, total_cost

def kruskals_algorithm(matrix):
    size = len(matrix)
    edges = []

    for i in range(size):
        for j in range(i + 1, size):
            if matrix[i][j] > 0:
                edges.append((matrix[i][j], i, j))

    edges.sort()

    parent = list(range(size))
    rank = [0] * size

    def find_set(node):
        if parent[node] != node:
            parent[node] = find_set(parent[node])
        return parent[node]

    def union_sets(u, v):
        root_u, root_v = find_set(u), find_set(v)

        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if find_set(u) != find_set(v):
            union_sets(u, v)
            mst.append((u + 1, v + 1, weight))
            total_cost += weight

    return mst, total_cost

adj_matrix = build_weighted_adj_matrix()
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

start_node = int(input("\nEnter the starting node for Prim's algorithm (1-9): ")) - 1

# Prim's Algorithm
prim_mst, prim_cost = prims_algorithm(adj_matrix, start_node)
print("\nMinimum Spanning Tree using Prim's Algorithm:")
for edge in prim_mst:
    print(f"Edge {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total weight of MST (Prim's): {prim_cost}")

# Kruskal's Algorithm
kruskal_mst, kruskal_cost = kruskals_algorithm(adj_matrix)
print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
for edge in kruskal_mst:
    print(f"Edge {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total weight of MST (Kruskal's): {kruskal_cost}")
