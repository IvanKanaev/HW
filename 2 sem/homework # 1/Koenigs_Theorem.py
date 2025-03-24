def bipartite(graph):
    n = len(graph)
    colors = [-1] * n

    for i in range(n):
        if colors[i] == -1:
            queue = [i]
            colors[i] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return False

    L = [i for i in range(n) if colors[i] == 0]
    R = [i for i in range(n) if colors[i] == 1]
    return (L, R)


def kuhn(graph):
    n = len(graph.keys())
    match = [-1] * n
    L = bipartite(graph)[0]

    def dfs(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or dfs(match[u]):
                    match[u] = v
                    return True
        return False

    for v in L:
        visited = [False] * n
        dfs(v)

    return match


def minpocr(graph):
    parts = bipartite(graph)
    if not parts:
        return 'граф не двудольный'

    L, R = parts
    n = len(graph)
    match = kuhn(graph)

    oriented_graph = {v: [] for v in range(n)}

    for v in L:
        for u in graph[v]:
            if match[u] == v:
                    oriented_graph[u].append(v)
            oriented_graph[v].append(u)

    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for u in oriented_graph[v]:
            if not visited[u]:
                dfs(u)

    free_L = []
    for v in L:
        if v not in match:
            free_L.append(v)

    for v in free_L:
        dfs(v)


    L_plus = [v for v in L if visited[v]]
    L_minus = [v for v in L if not visited[v]]
    R_plus = [v for v in R if visited[v]]
    R_minus = [v for v in R if not visited[v]]

    return L_minus + R_plus


G = {
    0: [1, 3, 5],
    1: [0, 2, 6],
    2: [1],
    3: [0, 4],
    4: [3, 5, 7],
    5: [0, 4],
    6: [1],
    7: [4]
}

print(minpocr(G))

