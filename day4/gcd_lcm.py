import math

a = 105
b = 30

print('gcd : ', math.gcd(b,a))
#print('lcm1 : ', math.lcm(b,a))#lcm 3.9
print('lcm2 : ', int(a*b/math.gcd(b,a)))
'''
def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p%q)


a = 30
b = 105

if a < b:
    a,b = b,a

g = gcd(a,b)
l = int(a*b/g)
print('gcd : ', g)
print('lcm : ', l)
'''