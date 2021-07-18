import sys
sys.stdin = open("input.txt", "r")
T = int(input())+1
for test_case in range(1,T):
    input()
    nums = list(map(int,input().split()))
    cnt = [0]*101
    for i in range(len(nums)):
        cnt[int(nums[i])] += 1

    maxIDX = 0
    for i in range(1,101):
        if (cnt[maxIDX] <= cnt[i]):
            maxIDX = i

    print("#%d %d" % (test_case, maxIDX))