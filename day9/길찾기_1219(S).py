import sys
sys.stdin = open('input.txt','r')

from collections import deque
maxN = 100
T = 11

for test_case in range(1, T):
    _, n = map(int, input().split())
    data = list(map(int, input().split()))
    g = [[]*maxN for _ in range(maxN)]

    for i in range(0, n*2, 2):
        g[data[i]].append(data[i+1])

    chk = 0
    stk = deque()
    stk.append(0)
    while stk:
        u = stk.pop()
        if u == 99:
            chk = 1
            break
        for i in g[u]:
            stk.append(i)

    print('#%d %d' % (test_case, chk))



