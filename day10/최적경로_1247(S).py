import sys
sys.stdin = open("input.txt", "r")


def btr(k, idx, sumDist):
    global customCnt
    global minDist
    if sumDist > minDist:
        return
    if k == customCnt:
        sumDist += dist[idx][k+1]
        if sumDist < minDist:
            minDist = sumDist
        return
    k += 1

    for i in range(1, customCnt+1):
        if visited[i]:
            visited[i] = False
            btr(k, i, sumDist+dist[idx][i])
            visited[i] = True


T = int(input()) + 1
for test_case in range(1, T):
    minDist = 987654321

    customCnt = int(input())
    data = list(map(int, input().split()))
    customX = [data[0]]
    customY = [data[1]]
    visited = [True]*(customCnt+1)
    for i in range(4, (customCnt+2)*2, 2):
        customX.append(data[i])
        customY.append(data[i+1])

    customX.append(data[2])
    customY.append(data[3])

    dist = [[0]*(customCnt+2) for _ in range(customCnt+2)]

    for i in range(customCnt+1):
        for j in range(i+1, customCnt+2):
            dist[i][j] = abs(customX[i] - customX[j]) + abs(customY[i] - customY[j])
            dist[j][i] = abs(customX[i] - customX[j]) + abs(customY[i] - customY[j])

    btr(0,0,0)

    print('#%d %d' % (test_case, minDist))