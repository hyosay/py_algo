src = [0, 'a', 'b', 'c']
n = 3
r = 2
a = [0] * (n + 1) #현재 까지의 정보
visited = [True] * (n+1) # 사용유무 판단

def user_print():
    print('[',end='')
    for i in range(1, r+1):
        print(src[a[i]], end=' ')
    print(']')


def perm_btr(k):
    if k == r:
        user_print()
        return

    k += 1
    for i in range(1, n+1):
        if visited[i]:
            visited[i] = False
            a[k] = i
            perm_btr(k)
            visited[i] = True

def pi_btr(k):
    if k == r:
        user_print()
        return

    k += 1
    for i in range(1, n+1):
        a[k] = i
        pi_btr(k)

perm_btr(0)
print('='*20)
pi_btr(0)