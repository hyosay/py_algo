import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = 10
for _ in range(T):
    tc = int(input())
    a = [input() for _ in range(100)]

    b = [''.join(x) for x in zip(*a)]

    maxLength = 0

    for mLen in range(100, 1, -1):
        for w in a:
            chk1 = False
            for i in range(100 - mLen + 1):
                chk2 = True
                for j in range(mLen // 2):
                    if w[i + j] != w[i + mLen - 1 - j]:
                        chk2 = False
                        break
                if chk2:
                    chk1 = True
                    break
            if chk1:
                if maxLength < mLen:
                    maxLength = mLen
                break
    for mLen in range(100, maxLength, -1):
        for w in b:
            chk1 = False
            for i in range(100 - mLen + 1):
                chk2 = True
                for j in range(mLen // 2):
                    if w[i + j] != w[i + mLen - 1 - j]:
                        chk2 = False
                        break
                if chk2:
                    chk1 = True
                    break
            if chk1:
                if maxLength < mLen:
                    maxLength = mLen
                break

    print('#%d %d' % (tc, maxLength))
