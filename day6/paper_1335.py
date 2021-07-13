n = int(input())

da = [list(map(int, input().split())) for _ in range(n)]

b = 0
w = 0
b_count = 0
w_count = 0


def re(data, n):
    global b
    global w
    global b_count
    global w_count

    b_count = 0
    w_count = 0

    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                b_count += 1
            else:
                w_count += 1

    if b_count == n * n:
        b = b + 1
    elif w_count == n * n:
        w = w + 1
    else:
        b_count = 0
        w_count = 0
        algo(n, data)


def algo(n, data):
    global b
    global w

    n = n // 2
    #1

    data1 = [data[i][:n] for i in range(n)]
    re(data1, n)

    #2
    data2 = [data[j][n:] for j in range(n)]
    re(data2, n)
    #3
    data3 = [data[k + n][:n] for k in range(n)]
    re(data3, n)
    #4
    data4 = [data[h + n][n:] for h in range(n)]
    re(data4, n)




algo(n, da)
print(w)
print(b)

