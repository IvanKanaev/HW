import heapq as h


def Dijkstra(G, s):
    V = len(G.keys())
    dist = [float('inf') for i in range(V)]
    prev = [None for i in range(V)]
    dist[s] = 0
    heap = [[s, 0]]

    while len(heap) != 0 :
        v, current_dist  = h.heappop(heap)

        if current_dist > dist[v]:
            continue

        for u, w in G[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                prev[u] = v
                h.heappush(heap, [u, dist[u]])

    return dist, prev
