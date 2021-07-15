import sys
sys.stdin = open('../day8/input.txt', 'r')

T, w = map(int, input().split())
a = []
ans = 0
for i in range(1, T + 1):
    we, key = map(int,input().split())
    a.append([we, key ,int(key / we)])
a.sort(key=lambda x : -x[2])



for i in a:
    if i[0] <= w:
        ans += i[1]
        w -= i[0]
    else:
        # ans += w*i[2]
        while w:
            ans += i[2]
            w -= 1

print(ans)


iLen = w + 1

