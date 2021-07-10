'''
cnt = 10
while cnt:
    print('cnt : ',cnt)
    if cnt == 8:
        cnt -= 5
        continue
    cnt -= 1
'''

_list = [1,2,3,4,5]

while _list:
    print('_list : ', _list)
    print('pop : ', _list.pop())