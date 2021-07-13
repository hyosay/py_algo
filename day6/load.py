import sys
sys.stdin = open('day6/input.txt', 'r')



def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())

    graph = []

    for i in range(N):
        graph.append(list(map(int, input().split())))

    graph2 = [h[:] for h in graph]



    key = [list(map(int, input().split())) for i in range(M)]

    result = []


    for j in range(0, M):
        dfs(key[j][0] - 1, key[j][1] - 1)

        if graph[key[j][2] - 1][key[j][3] - 1] == 0:
            result.append('0')
        else:
            result.append('1')
        graph = [k[:] for k in graph2]

    print('#{} {}'.format(T, ' '.join(result)))



"""input.txt
2
3 3
0 1 0
0 0 1
1 0 0
1 1 3 3
1 1 1 3
2 2 3 2
5 7
1 0 0 0 0
0 0 1 0 0
1 1 1 1 1
0 0 1 0 0
0 0 0 0 0
1 2 2 2
1 2 2 4
4 1 5 5
5 1 1 5
1 3 2 5
4 4 5 5
4 5 1 2
"""