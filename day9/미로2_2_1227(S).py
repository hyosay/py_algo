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

    dq = deque()
    dq.append(startY)
    dq.append(startX)
    data[1][1] = 1

    chk = 0
    while dq:
        cy = dq.popleft()
        cx = dq.popleft()
        if data[cy][cx] == 3:
            chk = 1
            break
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if data[ny][nx] != 1:
                dq.append(ny)
                dq.append(nx)
                if data[ny][nx] == 0:
                    data[ny][nx] = 1

    print('#%d %d' % (test_case, chk))
