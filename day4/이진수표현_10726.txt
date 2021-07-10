import sys
sys.stdin = open("input.txt", "r")
T = int(input())
ans = []
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    if bin(M)[-N:] == '1'*N:
        print('#%d ON' % test_case)
    else:
        print('#%d OFF' % test_case)
'''    
    ans.append("#%d ON" % test_case if bin(M)[-N:] == '1' * N else "#%d OFF" % test_case)

print('\n'.join(ans))
'''