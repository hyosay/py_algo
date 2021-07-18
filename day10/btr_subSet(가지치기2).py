n = 100
key = 50
src = []
a = [0] * (n+1)
for i in range(n+1):
    src.append(i)
cnt = 0
reCnt = 0
def btr_subSet(k, sumT):
    global cnt
    global reCnt
    cnt += 1
    if sumT > key:
        return

    if k == n:
        if sumT == key:
            reCnt += 1
        return
    k += 1

    a[k] = 0
    btr_subSet(k, sumT)
    a[k] = 1
    btr_subSet(k, sumT + src[k])

def btr_subSet1(k, sumT):
    global reCnt
    global cnt
    cnt += 1
    if sumT > key:
        return
    if sumT == key:
        reCnt += 1
        return
    if k == n:
        return
    k += 1

    a[k] = 0
    btr_subSet1(k, sumT)
    a[k] = 1
    btr_subSet1(k, sumT + src[k])
def btr_subSet2(k, sumT, restSum):
    global reCnt
    global cnt
    #cnt += 1
    if sumT > key:
        return
    if sumT == key:
        reCnt += 1
        return
    if sumT + restSum < key:
        return
    if k == n:
        return
    k += 1

    #a[k] = 0
    btr_subSet2(k, sumT, restSum - src[k])
    #a[k] = 1
    btr_subSet2(k, sumT + src[k], restSum - src[k])

reSum = 0
for i in range(1, n+1):
    reSum += src[i]
print('reSum : ', reSum)

btr_subSet2(0, 0, reSum)
print('cnt : ', cnt)
print('reCnt : ', reCnt)








