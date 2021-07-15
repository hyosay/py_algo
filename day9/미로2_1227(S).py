import sys
sys.stdin = open('input.txt','r')

from collections import deque
dy = [-1,1,0,0]
dx = [0,0,1,-1]
maxN = 100
T = 11

for test_case in range(1, T):
    input()
    data = [list(map(int,input())) for _ in range(maxN)]
    startY = 1
    startX = 1
    flag = False
    for i in range(1, maxN):
        for j in range(1, maxN):
            if data[i][j] == 3:
                endY = i
                endX = j
                flag = True
                break
        if flag:
            break

    dq = deque()
    dq.append(startY)
    dq.append(startX)
    data[1][1] = 1

    chk = 0
    while dq:
        cy = dq.popleft()
        cx = dq.popleft()
        if cy == endY and cx == endX:
            chk = 1
            break
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if data[ny][nx] != 1:
                dq.append(ny)
                dq.append(nx)
                data[ny][nx] = 1

    print('#%d %d' % (test_case, chk))
