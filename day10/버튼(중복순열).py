import sys
sys.stdin = open('input.txt','r')

from itertools import *
T = int(input()) + 1

for test_case in range(1, T):
    N, M, K = map(int, input().split())
    btnData = list(map(int, input().split()))

    cnt = 0
    for i in range(1, M):
        for j in product(btnData, repeat=i):
            if sum(j) % N == K:
                cnt += 1
    print('#%d %d' % (test_case, cnt))