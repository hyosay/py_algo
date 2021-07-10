import sys
sys.stdin = open("input2.txt", "r")

for _ in range(10):
    tc = int(input())
    input_list = [list(map(int, input().split())) for _ in range(100)]

    max, row, col= 0, 0, 0
    diagonal = 0
    back_diagonal = 0
    for i in range(100):
        col = 0
        row = 0
        diagonal += input_list[i][99 - i]
        back_diagonal += input_list[i][i]
        for j in range(100):
            col += input_list[i][j]
            row += input_list[j][i]

        if max <= col:
            max = col
        if max <= row:
            max = row


    if max <= diagonal:
        max = diagonal

    if max <= back_diagonal:
        max = back_diagonal
    print('#{} {}'.format(tc, max))





