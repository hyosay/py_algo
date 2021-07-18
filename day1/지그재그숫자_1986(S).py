import sys
sys.stdin = open("input.txt", "r")
T = int(input())+1
for test_case in range(1,T):
    num = int(input())
    ans = 0
    for i in range(1,num+1):
        if i&1:
            ans+=i
        else:
            ans+=(-i)
    print("#%d %d" % (test_case, ans))