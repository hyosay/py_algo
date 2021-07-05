import sys
sys.stdin = open("input2.txt", "r")

t = int(input())

b = [] * 100
for i in range(100):
    b.append(list(map(int, input().split())))

print(b)


adx = 0
for q in range(100):
    ad = 0
    for w in range(100):
        ad += b[q][w]
    if adx <= ad:
        adx = ad




