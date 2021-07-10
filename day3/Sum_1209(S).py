import sys
sys.stdin = open("input.txt", "r")


for _ in range(10):
    tc = int(input())
    input_list = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []
    # 가로합
    for idx in range(100):
        sum_list.append(sum(input_list[idx]))
    # 세로합
    for idx1 in range(100):
        inner_sum = 0
        for idx2 in range(100):
            inner_sum += input_list[idx2][idx1]
        sum_list.append(inner_sum)
    # 대각선합
    right_down = 0
    for idx3 in range(100):
        right_down += input_list[idx3][idx3]
    sum_list.append(right_down)
    right_up = 0
    for idx4 in range(100):
        right_up += input_list[idx4][99 - idx4]
    sum_list.append(right_up)

    print('#{} {}'.format(tc, max(sum_list)))