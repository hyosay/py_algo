a = '123'
b = '456'
c = a*3
d = a+b
e = 5
print(a)
print(b)
print(c)
print(d)
print(a*e)
#print(a+e) #동일자료형이 될때 연산 가능
'''
strA = '0123456789'
#strA[3] = 'a'#문자열은 불변
print(strA[3])
print(strA[:])
print(strA[:5])
print(strA[2:5])
print(strA[2:])
'''
'''
strA = 'abcd1234ab234abcde'
key = 'ab'

print(strA.count(key))
strA = '   abc d     '
print(strA.rstrip())
print(strA.lstrip(),'end')
print(strA.strip(),'end')
'''

strA = 'abcde'
strB = "abcde"
strC = "ab\"cd\"e"
strD = 'ab"cd"e'

print(strC)
print(strD)

numStr = '123 456\t789\n12345'
listA = numStr.split()
print(listA)
numStr = '123,456,789,12345'
listA = numStr.split(':')
print(listA)

numStr = '123456789123456789'
print(numStr.find('23', 3))
print(numStr.find('231'))
print('index : ',numStr.index('23'))
print(numStr[len(numStr)-1])
print(numStr[-1])


print(numStr.find('123', 10))