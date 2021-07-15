import sys
sys.stdin = open('input.txt','r')

for test_case in range(1, 11):
    n, data = input().split()
    while True:
        iLen = len(data)
        for i in range(iLen-1):
            if data[i] == data[i+1]:
                data = data[:i] + data[i+2:]
                break
        if iLen == len(data): break
    print('#%d %s' % (test_case, data))
