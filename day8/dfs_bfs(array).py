'''
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''
import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

V, E = map(int, input().split())
g = [[0]*(V+1) for _ in range(V+1)]

stk = []
queue = deque()
visited = [True]*(V+1)

def init():
    for i in range(1, V+1):
        visited[i] = True

def dfs1(start):
    init()
    stk.append(start)
    visited[start] = False
    print("dfs1 : [", end='')
    while stk:
        u = stk.pop()
        print(u, end=' ')
        for i in range(1, V+1):
           if visited[i] and g[u][i]:
                stk.append(i)
                visited[i] = False
    print(']')

def dfs2(start):
    init()
    stk.append(start)
    print("dfs2 : [", end='')
    while stk:
        u = stk.pop()
        if visited[u]:
            visited[u] = False
            print(u, end=' ')
            for i in range(1, V+1):
               if visited[i] and g[u][i]:
                    stk.append(i)
    print(']')

def dfs_rec(start):
    print(start, end=' ')
    visited[start] = False
    for i in range(1, V+1):
        if visited[i] and g[start][i]:
            dfs_rec(i)

def bfs(start):
    init()
    queue.append(start)
    visited[start] = False
    print("bfs : [", end='')
    while queue:
        u = queue.popleft()
        print(u, end=' ')
        for i in range(1, V+1):
           if visited[i] and g[u][i]:
                queue.append(i)
                visited[i] = False
    print(']')

for i in range(E):
    s, e = map(int, input().split())
    g[s][e] = 1
    g[e][s] = 1

'''
for i in range(1, V+1):
    for j in range(1, V+1):
        print(g[i][j], end=' ')
    print()
print()
'''
dfs1(1)
print('='*20)
dfs2(1)
print('='*20)
init()
print('dfs_rec : [', end='')
dfs_rec(1)
print(']')
print('='*20)
bfs(1)

















