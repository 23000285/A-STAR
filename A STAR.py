from collections import defaultdict

H_dist = {}

def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while open_set:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print("Path does not exist!")
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            return path

        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            elif g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n
                if m in closed_set:
                    closed_set.remove(m)
                    open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    return H_dist[n]

# --- INPUT SECTION WITH PROMPTS ---
graph = defaultdict(list)

print("Enter number of nodes and edges:")
n, e = map(int, input().split())

print("Enter each edge in the format: node1 node2 cost")
for i in range(e):
    u, v, cost = input().split()
    cost = int(cost)
    graph[u].append((v, cost))
    graph[v].append((u, cost))  # For undirected graph

print("Enter heuristic values for each node:")
for i in range(n):
    node, h = input().split()
    H_dist[node] = int(h)

Graph_nodes = graph

print("Enter the start node:")
start = input()

print("Enter the goal node:")
goal = input()

# --- RUN A* ---
aStarAlgo(start, goal)
