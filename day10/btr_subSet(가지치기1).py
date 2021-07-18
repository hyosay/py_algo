n = 10
key = 10
src = []
a = [0] * (n+1)
for i in range(n+1):
    src.append(i)

cnt = 0
reCnt = 0
def user_print():
    global cnt
    global reCnt

    cnt += 1

    SUM = 0
    for i in range(1, n+1):
        if a[i]:
            SUM += src[i]
    if SUM <= key:
        reCnt += 1
        print('{', end='')
        for i in range(1, n+1):
            if a[i]:
                print(src[i], end=' ')
        print('}')

def btr_subSet(k):
    if k == n:
        user_print()
        return
    k += 1

    for i in range(2):
        a[k] = i
        btr_subSet(k)

def check(k):
    SUM = 0
    for i in range(1, k+1):
        if a[i]:
            SUM += src[i]
    return SUM

def btr_subSet1(k):
    if check(k) > key:
        return

    if k == n:
        user_print()
        return
    k += 1

    a[k] = 0
    btr_subSet1(k)
    a[k] = 1
    btr_subSet1(k)
def btr_subSet2(k, sumT):
    if sumT > key:
        return

    if k == n:
        user_print()
        return
    k += 1

    a[k] = 0
    btr_subSet2(k, sumT)
    a[k] = 1
    btr_subSet2(k, sumT + src[k])
def btr_subSet3(k, sumT):
    global reCnt
    if sumT > key:
        return

    if k == n:
        reCnt += 1
        return
    k += 1

    a[k] = 0
    btr_subSet3(k, sumT)
    a[k] = 1
    btr_subSet3(k, sumT + src[k])

btr_subSet3(0, 0)

print('cnt : ', cnt)
print('reCnt : ', reCnt)








