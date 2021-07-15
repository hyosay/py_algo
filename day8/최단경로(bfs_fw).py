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
g = [[0]*(V+1) for _ in range(V+1)]
dist = [INF]*(V+1)
p = [0]*(V+1)

def bfs(start, end):
    que = deque()
    dist[start] = 0
    que.append(start)
    while que:
        u = que.pop()
        for i in range(1, V+1):
            if dist[i] > dist[u] + g[u][i]:
                dist[i] = dist[u] + g[u][i]
                que.append(i)
                p[i] = u
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

'''
def f_w(start, end):
    for k in range(1, V+1):#경유지
        for s in range(1, V+1):#출발지
            if s!=k:
                for e in range(1, V+1):#도착지
                    if e!=k and e!=s:
                        if g[s][e] > g[s][k]+g[k][e]:
                            g[s][e] = g[s][k] + g[k][e]
    print('ans : ', g[start][end])
'''
def f_w(start, end):
    for k in range(1, V+1):#경유지
        for s in range(1, V+1):#출발지
            for e in range(1, V+1):#도착지
                if g[s][e] > g[s][k]+g[k][e]:
                    g[s][e] = g[s][k] + g[k][e]
    print('ans : ', g[start][end])

for i in range(E):
    s, e, v = map(int, input().split())
    g[s][e] = v
'''
for i in range(1, V+1):
    for j in range(1, V+1):
        print(g[i][j] , end=' ')
    print()
print()
'''
for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j and g[i][j] == 0:
            g[i][j] = INF
'''            
for i in range(1, V+1):
    for j in range(1, V+1):
        print(g[i][j] , end=' ')
    print()
print()
'''

bfs(1, 7)
print('='*20)
f_w(1,7 )