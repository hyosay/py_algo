import sys
sys.stdin = open("input.txt", "r")
from collections import deque
T = 11
for test_case in range(1, T):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    g = [[] for _ in range(V+1)]
    indegree = [0]*(V+1)
    for i in range(0, E*2, 2):
        s = data[i]
        e = data[i+1]
        g[s].append(e)
        indegree[e] += 1

    stk = deque()
    for i in range(1, V+1):
        if indegree[i] == 0:
            stk.append(i)
    print('#%d' % test_case, end=' ')
    while stk:
        u = stk.pop()
        print(u, end=' ')
        for i in g[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                stk.append(i)
    print()
