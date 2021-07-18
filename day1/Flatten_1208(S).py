import sys
sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    dump = int(input())
    boxPos = sorted(list(map(int, input().split())))

    while dump :
        boxPos[-1] -= 1
        boxPos[0] += 1
        boxPos.sort()
        dump -= 1

    print("#%d %d" % (test_case, (max(boxPos) - min(boxPos))))