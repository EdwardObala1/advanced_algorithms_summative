from collections import defaultdict
from heapq import heappop, heappush
import os

def shortestReach(n, edges, s):
    graph = defaultdict(list)
    for (u, v), w in edges.items():
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    visited = [False for _ in range(n + 1)]
    distance = [float("inf") for _ in range(n + 1)]
    distance[s] = 0
    minHeap = [(distance[s], s)]
    
    while minHeap:
        d, u = heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        for w, v in graph[u]:
            if not visited[v] and distance[v] > d + w:
                distance[v] = d + w
                heappush(minHeap, (distance[v], v))
    del distance[s]
    del distance[0]
    return [-1 if d == float("inf") else d for d in distance]

shortestReach()