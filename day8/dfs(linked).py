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
g = [[] for _ in range(V+1)]
stk = []
visited = [True]*(V+1)
for i in range(E):
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)
'''
for i in range(1, V+1):
    print(i,end=': [')
    for j in g[i]:
       print(j,end=' ')
    print(']')
print()
'''

stk.append(1)
visited[1] = False
print('dfs : [', end="")
while stk:
    u = stk.pop()
    print(u, end=' ')
    for i in g[u]:
        if visited[i]:
            stk.append(i)
            visited[i] = False
print(']')






