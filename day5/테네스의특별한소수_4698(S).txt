import sys
sys.stdin = open("input.txt", "r")
import math
max_num = 1000001
prime_num = [1]*max_num#[1 for _ in range(max_num)]

iLen = int(math.sqrt(max_num))+1
for i in range(2, iLen):
    if prime_num[i]:
        for j in range(i * i, max_num, i):
            prime_num[j] = 0

prime_num[1] = 0

T = int(input())+1

for test_case in range(1, T):
    D, A, B = map(int, input().split())
    D = str(D)
    cnt = 0
    for i in range(A, B + 1):
        if prime_num[i]:
            if D in str(i):
                cnt += 1

    print('#%d %d' % (test_case, cnt))
