import sys
sys.stdin = open('input.txt','r')

from collections import deque

for test_case in range(1, 11):
    n, data = input().split()
    dq = deque()
    dq.append(0)
    dq.append(data[0])
    for i in range(1, len(data)):
        if dq[-1] == data[i]:
            dq.pop()
        else:
            dq.append(data[i])
    dq.popleft()
    ans = ''.join(dq)
    print('#%d %s' % (test_case, ans))
