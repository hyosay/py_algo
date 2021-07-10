import sys
sys.stdin = open("input.txt", "r")
T = 11#int(input())

for test_case in range(1, T):
    N = int(input())
    data = list(map(int, input().split()))
    iLen = N-2
    ans = 0
    for i in range(2, iLen):
        temp = max(data[i-2],data[i-1],data[i+1],data[i+2])
        if data[i] > temp:
            ans += (data[i] - temp)
    print('#%d %d' % (test_case, ans))