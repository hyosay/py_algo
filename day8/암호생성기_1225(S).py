import sys
sys.stdin = open('../input.txt', 'r')

from collections import deque

for test_case in range(1, 11):
    n = input()
    dq = deque(map(int, input().split()))
    MIN = 987654321
    for i in range(8):
        if MIN > dq[i]:
            MIN = dq[i]
    MIN = int(MIN / 15) - 1
    for i in range(8):
        dq[i] -= MIN*15
    k = 0
    while dq[-1]:
        k = k % 5 + 1
        t = dq[0] - k
        dq.popleft()
        if t < 0:
            t = 0
        dq.append(t)

    print('#%d' % test_case , end=' ')
    for i in range(8):
        print(dq[i], end=' ')
    print()
