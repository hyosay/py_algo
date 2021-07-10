#           상 하 좌 우
dx = list([0, 0, -1, 1])
dy = list([1,-1, 0, 0])

sx = 1
sy = 1

for i in range(4):
    nx = sx+dx[i]
    ny = sy+dy[i]

    print(nx,":",ny)
