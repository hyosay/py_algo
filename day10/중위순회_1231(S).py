import sys
sys.stdin = open('input.txt','r')


T = 11
def inPrint(root):
    if src[root] != 0:
        inPrint(root*2)
        print(src[root], end='')
        inPrint(root*2+1)

for test_case in range(1, T):
    N = int(input())
    src = [0]*(N+1)*2
    for i in range(1, N+1):
        temp = input().split()
        src[i] = temp[1]
    
    print('#%d'%test_case, end=' ')
    inPrint(1)
    print()