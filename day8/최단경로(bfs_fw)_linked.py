'''
7 14
1 2 3
1 3 1
2 3 1
2 4 2
2 5 4
3 2 3
3 4 4
3 6 6
4 5 7
4 6 2
5 6 4
5 7 5
6 5 3
6 7 8
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque
INF = 987654321
V, E = map(int, input().split())
g = [[]*(V+1) for _ in range(V+1)]
dist = [INF]*(V+1)
p = [0]*(V+1)

def bfs(start, end):
    que = deque()
    dist[start] = 0
    que.append(start)
    while que:
        u = que.pop()
        for i in g[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]
                que.append(i[0])
                p[i[0]] = u
    print('idx :\t[', end='')
    for i in range(1, V+1):
        print("%d\t" % i, end=' ')
    print(']')
    print('dist :\t[', end='')
    for i in range(1, V+1):
        print("%d\t" % dist[i], end=' ')
    print(']')
    print('p :\t[', end='')
    for i in range(1, V+1):
        print("%d\t" % p[i], end=' ')
    print(']')
    print('ans : %d' % dist[end])
    stk2 = []

    while end:
        stk2.append(end)
        end = p[end]
    stk2.reverse()
    print(stk2)


for i in range(E):
    s, e, v = map(int, input().split())
    g[s].append((e,v))
'''
for i in range(1, V+1):
    print(i,":",end="")
    for j in g[i]:
        print(j,end=" ")
    print()
print()
'''
bfs(1, 7)