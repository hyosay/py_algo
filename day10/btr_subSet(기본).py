n = 10
src = []
a = [0] * (n+1)
for i in range(n+1):
    src.append(i)

def user_print():
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

btr_subSet(0)








