'''
7 11
1 2 32
1 3 31
1 6 60
1 7 51
2 3 21
3 5 46
3 7 25
4 5 34
4 6 18
5 6 40
5 7 51
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque
import heapq
INF = 987654321
V, E = map(int, input().split())
g = [[]*(V+1) for _ in range(V+1)]
dist = [INF]*(V+1)
p = [0]*(V+1)

def prim(start):
    visited = [True]*(V+1)
    pq = []
    heapq.heappush(pq, (0, start))

    dist[start] = 0

    while pq:
        u = heapq.heappop(pq)[1]
        if not visited[u]: continue

        visited[u] = False

        for i in g[u]:
            if visited[i[0]] and dist[i[0]] > i[1]:
                dist[i[0]] = i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
                p[i[0]] = u
    sumT = 0
    print('idx :\t[', end='')
    for i in range(1, V+1):
        print("%d\t" % i, end=' ')
    print(']')
    print('dist :\t[', end='')
    for i in range(1, V+1):
        sumT += dist[i]
        print("%d\t" % dist[i], end=' ')
    print(']')
    print('p :\t[', end='')
    for i in range(1, V+1):
        print("%d\t" % p[i], end=' ')
    print(']')

    print('dist_sum : ', sumT)

for i in range(E):
    s, e, v = map(int, input().split())
    g[s].append((e, v))
    g[e].append((s, v))
'''
for i in range(1, V+1):
    print(i,":",end="")
    for j in g[i]:
        print(j,end=" ")
    print()
print()
'''
prim(3)