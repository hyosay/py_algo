import sys
sys.stdin = open("input.txt", "r")
from collections import deque
T = int(input())+1
for test_case in range(1, T):
    V, E, S1, S2 = map(int, input().split())
    data = list(map(int, input().split()))
    leftC = [0]*(V+1)
    rightC = [0]*(V+1)
    p = [0]*(V+1)
    for i in range(0, E*2, 2):
        s = data[i]
        e = data[i+1]
        if leftC[s]:
            rightC[s] = e
        else:
            leftC[s] = e
        p[e] = s

    ancestor1 = []
    ancestor2 = []
    start = p[S1]
    while start:
        ancestor1.append(start)
        start = p[start]

    start = p[S2]
    while start:
        ancestor2.append(start)
        start = p[start]

    flag = False
    ans = 0
    for i in ancestor1:
        for j in ancestor2:
            if i == j:
                ans = i
                flag = True
                break
        if flag:
            break
    q = deque()
    cnt = 0
    q.append(ans)
    while q:
        u = q.pop()
        cnt += 1

        if leftC[u]:
            q.append(leftC[u])
        if rightC[u]:
            q.append(rightC[u])

    print('#%d %d %d' % (test_case, ans, cnt))
