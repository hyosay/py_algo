'''
for i in range(2):#start = 0, end-1, 증감 1
    print(i)
print('='*10)
for i in range(1,3):#start = 1, end-1, 증감 1
    print(i)
print('='*10)
for i in range(4,20, 5):#start = 1, end-1, 증감 5
    print(i)
print('='*10)
for i in range(10, 0, -1):#start = 10, end 1, 증감 -5
    print(i, end=' ')
print()
print('='*10)
'''
'''
_list = ['a','b','c']

for c in _list:
    print(c)
'''
'''
_dict = {1:'a',2:'b',3:'c'}
for d in _dict:
    print(d)
print('='*10)
for k in _dict.keys():
    print(k)
print('='*10)
for v in _dict.values():
    print(v)
print('='*10)
for k,v in _dict.items():
    print(k,' : ', v)
print('='*10)
'''
'''
#enum
_list = ['a','b','c']
for i, v in enumerate(_list):
    print(i,':',v)
'''
'''
for i in range(10):
    for j in range(10):
        print(i,':',j)
        if j==3:
            break
'''
'''
chk = False
for i in range(10):
    for j in range(10):
        print(i,':',j)
        if j==3:
            chk = True
            break
    if chk:
        break;
'''
'''
for i in range(10):
    for j in range(4):
        print(i,':', j)
        if j == 4: break
    else: break
print('end')
'''
