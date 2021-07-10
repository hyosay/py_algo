'''
def add(a,b):
    return a+b

ans = add(2,5)
print('ans : ', ans)

add2 = lambda x,y : x+y
print('ans lam :', add2(2,4))
'''
'''
_list1 = []
for i in range(5):
    _list1.append(i*2)
print('list1', _list1)
_list2 = [i*2 for i in range(5)]
print('list2', _list2)

_list3 = list(map(lambda x : x*2, range(5)))
print('list3', _list3)

listA = [1,2,3]
listB = [2,4,6,]
_list4 = list(map(lambda x,y : x+y, listA,listB))
print('list4', _list4)

_list5 = list(map(lambda x : x&1==1, range(10)))
print('list5 : ', _list5)
_list6 = list(filter(lambda x : x&1, range(10)))
print('list6 : ', _list6)
'''

list1 = [1,2,3]
list2 = [1,2,3]
list3 = [1,2,3]

for i in zip(list1,list2,list3):
    print(i)

listStr = ['abcd','abcd', 'abcd','abcd']

for i in zip(listStr[0], listStr[1], listStr[2], listStr[3]):
    print(i)
print('='*10)
for i in zip(*listStr):
    print("".join(i))
print('='*10)


list4 = ['a','1','b','2']
strTemp = "".join(list4)
print(strTemp)

















