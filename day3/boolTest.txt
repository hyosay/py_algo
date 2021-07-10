'''
#정수
a = 1
_bool = bool(a)
print(_bool)
a = -1
_bool = bool(a)
print(_bool)
a = 0
_bool = bool(a)
print(_bool)
'''
'''
#실수
a = 1.
_bool = bool(a)
print(_bool)
a = 0.
_bool = bool(a)
print(_bool)
'''
'''
a = [0]
_bool = bool(a)
print(_bool)
a = tuple(a)
_bool = bool(a)
print(_bool)
a = {}
_bool = bool(a)
print(_bool)
a = [1]
_bool = bool(a)
print(_bool)
'''
'''
a = None
_bool = bool(a)
print(_bool)
'''
'''
a = [1]
b = [2]
c = []
_bool = bool(a) and bool(b)
print('and : ', _bool)
_bool = bool(a) and bool(c)
print('and : ', _bool)
_bool = bool(a) or bool(b)
print('or : ', _bool)
_bool = bool(a) or bool(c)
print('or : ', _bool)
print('not : ', not _bool)
'''

_list = [1,2,3]
print('in : ' , 1 in _list)
print('in : ' , 4 in _list)
