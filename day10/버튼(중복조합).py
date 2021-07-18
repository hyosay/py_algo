import sys
sys.stdin = open('input.txt','r')
from itertools import *
import math
T = int(input()) + 1

for test_case in range(1, T):
    N, M, K = map(int, input().split())
    btnData = list(map(int, input().split()))

    cnt = 0
    for i in range(1, M):
        for j in combinations_with_replacement(btnData, i):

            if sum(j) % N == K:
                _dict = {}
                for k in j:
                    if k in _dict:
                        _dict[k] += 1
                    else:
                        _dict[k] = 1
                tmp = math.factorial(len(j))
                for k in _dict.values():
                    tmp /= math.factorial(k)
                cnt += tmp
    print('#%d %d' % (test_case, cnt))

