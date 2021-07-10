dictA = {'1':'a', '4': 'c', '2':'b', '1':'e'}
dictA['3'] = 'ab'
dictA[100] = 'ab'
print(dictA)
'''
print(dictA['2'])
print(dictA.keys())
print(dictA.values())
print(dictA.items())

for i in dictA:
    print(dictA[i])
print('='*10)
for i in dictA.keys():
    print(dictA[i])
print('='*10)
for i in dictA.values():
    print(i)
print('='*10)
for key, val in dictA.items():
    print(key , ': ', val)
print('='*10)
'''