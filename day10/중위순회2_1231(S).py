import sys
sys.stdin = open('input.txt','r')


T = 11
def inPrint(root):
    global ans
    if root <= N:
        inPrint(root*2)
        ans += src[root]
        inPrint(root*2+1)

for test_case in range(1, T):
    N = int(input())
    src = [0]*(N+1)
    for i in range(1, N+1):
        temp = input().split()
        src[i] = temp[1]
    ans = ''
    inPrint(1)
    print('#%d %s' % (test_case, ans))