import sys
sys.stdin = open("input.txt", "r")

from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

T = int(input())+1
for test_case in range(1, T):
    N, M = map(int, input().split())
    totalCnt = N*N
    blockCnt = 0

    data = [[1]*(N+2)]
    for i in range(N):
        data.append([1]+list(map(int, input().split()))+[1])
    data.append([1]*(N+2))
    for i in range(1, N+1):
        for j in range(1, N+1):
            if data[i][j]:
                blockCnt += 1
    findCnt = blockCnt
    groupNum = 2

    s = deque()
    flag = False
    for i in range(1, N+1):
        for j in range(1, N+1):
            if data[i][j] == 0:
                s.append(i)
                s.append(j)
                findCnt += 1
                data[i][j] = groupNum;

            while s:
                cx = s.pop()
                cy = s.pop();
                for k in range(4):
                    ny = cy + dy[k]
                    nx = cx + dx[k]
                    if data[ny][nx] == 0:
                        s.append(ny)
                        s.append(nx)
                        findCnt += 1
                        data[ny][nx] = groupNum
            groupNum += 1
            if totalCnt == findCnt:
                flag = True
                break
        if flag:
            break
    print("#%d" % test_case , end=' ')

    for i in range(M):
        a, b, c, d = map(int, input().split())
        if data[a][b] == data[c][d]:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()