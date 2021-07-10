listA = ['a','b','c','a','c']
print(listA)
listA.remove('a')
#listA.remove('d')#error
print(listA)
listA.pop()
print(listA)
listA.pop(4)
print(listA)

'''
listA = [1,2,3]
listA.insert(4,'b')
print(listA)

listB = [4,5,6]
listA.extend(listB)
listC = listA+listB
print(listA)
print(listC)
'''
'''
listA = [1,2,3]
strA = 'abcd'
listB = list(listA)
listC = list(strA)
listD = listA
print('A : ',listA)
print('B : ',listB)
print('C : ',listC)
print('D : ',listD)

print('A addr : ',id(listA))
print('B addr : ',id(listB))
print('D addr : ',id(listD))
listD[2] = 5

print('A : ',listA)
print('D : ',listD)
'''
'''
listA = [2,3,1,4,5,6,7,8]
sortListA = sorted(listA)
sortListB = sorted(listA, reverse=True)

print(listA)
print(sortListA)
print(sortListB)'''
'''
print('정렬전 : ',listA)
listA.sort()
print('정렬후 asc : ',listA)
listA.sort(reverse=True)
print('정렬후 desc : ',listA)
'''
'''
listA = [1,2,3]
listB = [4,5,6]
listC = listA+listB
listC.append(3)
print(listC)
'''

'''
listA = [1,2.,3]

print('len : ',len(listA))
print(listA)
print(type(listA)," : ", type(listA[0]))

listA = []
for i in range(5):
    listA.append(i)
print(listA)

listA = [0,0,0,0,0]
print(listA)
listA = [0]*5
print(listA)
listA = []
for i in range(5):
    listA.append(0)
print(listA)
listA = [0 for _ in range(5)]
print(listA)
'''