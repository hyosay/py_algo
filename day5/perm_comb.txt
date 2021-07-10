maxL = 100
src = [0,'a','b','c']
temp = [0]*maxL
n = 0
r = 0
def userPrint():
    print('[', end="")
    for i in range(r, 0, -1):
        print(temp[i], end=' ')
    print(']')

def perm(n, r):
    if r == 0:
        userPrint()
        return
    for i in range(n,0, -1):
        src[n], src[i] = src[i], src[n]
        temp[r] = src[n]
        perm(n - 1, r - 1)
        src[n], src[i] = src[i], src[n]

'''
def pi(n, r):
    if r == 0:
        userPrint()
        return
    for i in range(n,0, -1):
        src[n], src[i] = src[i], src[n]
        temp[r] = src[n]
        pi(n , r - 1)
        src[n], src[i] = src[i], src[n]
'''
def pi(n, r):
    if r == 0:
        userPrint()
        return
    for i in range(n,0, -1):
        temp[r] = src[i]
        pi(n , r - 1)

def comb(n, r):
    if r==0:
        userPrint()
        return
    if n<r:
        return
    temp[r] = src[n]
    #포함
    comb(n-1, r-1)
    #비포함
    comb(n-1, r)
def h(n, r):
    if r==0:
        userPrint()
        return
    if n==0:
        return
    temp[r] = src[n]
    #포함
    h(n, r-1)
    #비포함
    h(n-1, r)


n = 3
r = 2
'''
perm(n, r)
print('='*10)
pi(n, r)
print('='*10)
comb(n, r)
print('='*10)
h(n, r)
print('='*10)
'''
'''
for i in range(n+1):
    r = i
    comb(n, r)
'''

def comb_cal(n, r):
    if r == 0 or n == r:
        return 1
    return comb_cal(n-1, r-1) + comb_cal(n-1, r)

dpMemo = [[0]*101]*101

def comb_cal_dp(n, r):
    if r == 0 or n == r:
        return 1
    if dpMemo[n][r] == 0:
        dpMemo[n][r] = comb_cal_dp(n-1, r-1) + comb_cal_dp(n-1, r)
    return dpMemo[n][r]

n = 100
r = 50
print('%d C %d = %d' % (n, r ,comb_cal_dp(n, r)))

# 독립시행 확률 : 이항분포 확률 nCr*p^r*q^(n-r)







