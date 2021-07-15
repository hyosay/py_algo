import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

for test_case in range(1, 11):
    n = input()
    dq = deque(map(int, input().split()))
    MIN = 987654321
    for i in range(0):
        if MIN > dq[i]:
            MIN = dq[i]
