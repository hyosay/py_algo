import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, 1 + T):
    n = int(input())
    a = list(map(int ,input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([a[i], b[i]])
    env = input()
    print(c)
