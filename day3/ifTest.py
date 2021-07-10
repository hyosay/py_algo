'''
if []:
    pass

a = [1]
if a:
    print('full')
else:
    print('empty')
print("end")
'''
'''
_list = [1,2,3]
print(_list)
data = 3
if data not in _list:
    _list.append(data)
print(_list)
'''
'''
a = 15
if a>=10 and a<20:
    print("10대")
elif a >= 20 and a < 30:
    print("20대")
elif a>=30 and a<40:
    print("30대")
elif a>=40 and a<50:
    print("40대")
elif a>=51 and a<60:
    print("50대")
else:
    print('60대 이상')
'''

data = {1:(10,'M')}
age, sex = data[1]
if age == 10:
    if sex == 'M':
        print('ok')

if age == 10 and sex == 'M':
    print('ok')

a = 10
if a!=20:
    print("error")