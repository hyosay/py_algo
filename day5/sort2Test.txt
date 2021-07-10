_list = [2,3,4,1,5]
sortedList = sorted(_list)
print(_list)
print(sortedList)

_set = {3,4,5,3,4,5,7,1,2}
print(_set)
sortedSet = sorted(_set)
print(sortedSet)

_tuple = (3,4,1,2,5,6,9)
sortedTuple = sorted(_tuple)
print(sortedTuple)

_dict = {1:'c', 3:'a', 2:'b'}

sortedDict = sorted(_dict.items(), key= lambda x : x[1])
print(sortedDict)


_list2 = [[2,1],[3,3],[1,2], [2,2]]
print('_list2 : ',_list2)
#default [0]기준
sortedlist2 = sorted(_list2)
sortedlist2 = sorted(_list2, key= lambda x : x[0])
print('sortedlist2 : ',sortedlist2)
#default [1]기준, asc
sortedlist2 = sorted(_list2, key= lambda x : x[1])
print('sortedlist2 : ',sortedlist2)
#default [1]기준, desc
sortedlist2 = sorted(_list2, key= lambda x : -x[1])
print('sortedlist2 : ',sortedlist2)
#default [0] asc , [1] desc
sortedlist2 = sorted(_list2, key= lambda x : (x[0],-x[1]))
print('sortedlist2 : ',sortedlist2)
'''
_list = ['abc','b','ab']

print(_list)
# default asc
_list.sort()
# desc
_list.sort(reverse=True)
#문자열의 길이에 따른 정렬
_list.sort(key=len)
_list.sort(key=len, reverse=True)
print(_list)
'''
























