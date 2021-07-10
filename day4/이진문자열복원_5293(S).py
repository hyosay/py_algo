import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    if A and not B and not C and not D:
        result = '0' * (A + 1)
    elif D and not A and not B and not C:
        result = '1' * (D + 1)
    elif B == C and B:
        result = '0' * (A + 1) + '10' * (B - 1) + '1' * (D + 1) + '0'
    elif B - C == 1:
        result = '0' * (A + 1) + '10' * C + '1' * (D + 1)
    elif C - B == 1:
        result = '1' * (D + 1) + '01' * B + '0' * (A + 1)
    else:
        result = 'impossible'

    print('#%d %s' % (test_case, result))
