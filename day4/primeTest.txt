import math
def isPrime1(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
def isPrime2(num):
    iLen = int(math.sqrt(num))+1
    if num == 1:
        return False
    for i in range(2, iLen):
        if num%i == 0:
            return False
    return True

n = 100000007

if isPrime1(n):
    print('Y')
else:
    print('N')
