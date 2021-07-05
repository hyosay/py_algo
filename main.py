import sys

# 키보드로 txt파일 불러오기
sys.stdin = open("input.txt", "r")

t = int(input())

for test in range(1, t + 1):
    n = int(input())
    k = list(map(int ,input().split()))
    count = [[i, 0] for i in range(101)]
    max = 0
    for o in k:
        count[o][1] += 1
    count_sort = sorted(count, key = lambda x : x[1], reverse= False)
    print("#{0} {1}".format(n, count_sort[100][0]))

