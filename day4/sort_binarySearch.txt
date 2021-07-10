
def selectSort(src):
    srcLen = len(src)
    for i in range(srcLen-1):
        maxIdx = 0
        for j in range(1,srcLen-i):
            if src[maxIdx] < src[j]:
                maxIdx = j
        src[srcLen-1 - i] , src[maxIdx] = src[maxIdx], src[srcLen-1 - i]

        print(i,"번째 :", src)

def bubbleSort(src):
    srcLen = len(src)
    for i in range(srcLen-1):
        for j in range(srcLen-i-1):
            if src[j] > src[j+1]:
                src[j], src[j+1] = src[j+1], src[j]
        print(i ,'번째 : ', src)

def binarySearch(src, sKey):
    s = 0
    e = len(src)-1

    while s <= e:
        c = int((s+e)/2)
        if src[c] == sKey:
            return c
        elif src[c] < key:
            s = c+1
        else:
            e = c-1
    return -1

data = [3,10,1,2,6,7,8,5,9]
print("정렬전 : ",data)
key = 10
selectSort(data)
idx = binarySearch(data, key)
print('idx : ', idx)
#selectSort(data)
#bubbleSort(data)

'''
data = [i for i in range(10)]

print(data)

data[2] = 20
print(data)
key = 20
'''

'''
ans = "N"
for d in data:
    if d == key:
        ans = 'Y'
        break

print('ans : ', ans)
'''

