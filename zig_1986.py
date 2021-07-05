import sys
sys.stdin = open("input (1).txt", 'r')
test = 10
t = 0
count =[]
for k in range(1, test + 1):
    t = int(input())
    count = list(map(int, input().split()))
    for i in range(t):
        min_count = min(count)
        max_count = max(count)
        for j in range(100):
            if count[j] == min_count:
                count[j] += 1
                break
        for j in range(100):
            if count[j] == max_count:
                count[j] -= 1
                break
    print('#{} {}'.format(k, max(count) - min(count)))






