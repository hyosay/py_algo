'''
def add(a, b):
    print(a,':', b)
    return a+b

aV = 10
bV = 20

ans = add(aV, bV)
print('ans : ', ans)
'''
'''
a = 20
def add(b):
    global a ;
    a = b
    print('f : ',a)

print(a)
add(30)
print(a)
'''

'''
def print_rec(n):
    if n == 101:
        return
    print(n)
    print_rec(n+1)


print_rec(1)
'''
'''
import time

start = time.time()
cnt = 0
dp = [0]*101
def fibo_rec(n):
    global cnt
    cnt+=1
    if n < 2:
        return n
    return fibo_rec(n-1)+fibo_rec(n-2)
num = 30
ans = fibo_rec(num)
print('ans : ', ans)
end = time.time()

print('cnt : ', cnt)
print('time : ', (end-start))
'''
import time

start = time.time()
cnt = 0
dp = [0]*101
def fibo_rec(n , memo):
    global cnt
    cnt+=1
    if n < 2:
        return n
    if memo[n] == 0:
        memo[n] = fibo_rec(n-1, memo)+fibo_rec(n-2, memo)
    return memo[n]
num = 50
ans = fibo_rec(num , dp)
print('ans : ', ans)
end = time.time()

print('cnt : ', cnt)
print('time : ', (end-start))