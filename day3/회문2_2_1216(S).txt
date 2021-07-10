import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')


def get_solution(arr, m):
    for word in arr:  
        for s in range(100 - m + 1):
            for k in range(m // 2):
                if word[s + k] != word[s + m - 1 - k]:
                    break
            else:
                return m
    return 0


T = 10
for _ in range(T):
    tc = int(input())
    a = [input() for _ in range(100)]
    b = [''.join(x) for x in zip(*a)]

    maxLength = 1
    for m in range(2, 101):
        if m > maxLength + 2:
            break
        if maxLength < get_solution(a, m):
            maxLength = m

    for m in range(maxLength + 1, 101):
        if m > maxLength + 2:
            break
        if maxLength < get_solution(b, m):
            maxLength = m

    print('#%d %d' % (tc, maxLength))
