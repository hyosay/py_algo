from itertools import permutations as perm
from itertools import combinations as comb
from itertools import product as prod
from itertools import combinations_with_replacement as cwr

_list = ['a','b','c']

for i in perm(_list, 2):
    print(i)
print('='*10)
for i in comb(_list, 2):
    print(i)
print('='*10)
for i in prod(_list, repeat=2):
    print(i)
print('='*10)
for i in cwr(_list, 2):
    print(i)
