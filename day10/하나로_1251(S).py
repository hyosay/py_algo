import sys
sys.stdin = open('input.txt','r')

import heapq
T = int(input()) + 1

for test_case in range(1, T):
    N = int(input())
    xList = list(map(int, input().split()))
    yList = list(map(int, input().split()))
    E = float(input())
    g = [[0]*N for _ in range(N)]
    dist = [987654321*987654321.]*N
    for i in range(N-1):
        for j in range(i+1, N):
            g[i][j] = g[j][i] = (xList[i] - xList[j])**2 + (yList[i] - yList[j])**2

    pq = []
    dist[0] = 0
    visited = [True]*N
    heapq.heappush(pq, (0, 0))
    while pq:
        u = heapq.heappop(pq)[1]
        if not visited[u]: continue
        visited[u] = False

        for i in range(N):
            if visited[i] and dist[i] > g[u][i]:
                dist[i] = g[u][i]
                heapq.heappush(pq, (dist[i], i))

    print('#%d %.0f' % (test_case,sum(dist)*E))

