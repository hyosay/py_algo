src = [2, 3, 4, 1, 5, 6, 7, 8]
n = len(src)
temp = [0]*n

def mergeSort(start, end):
    if start < end:
        mid = int((start + end) / 2)
        mergeSort(start,  mid) #왼쪽 영역
        mergeSort(mid + 1, end) #오른쪽 영역
        p = start
        q = mid + 1
        idx = start

        while p <= mid or q <= end:
            if q > end or (p <= mid and src[p] < src[q]):
                temp[idx] = src[p]
                idx ++ 1
                p += 1

        else:
            temp[idx] = src[q]
            q += 1
        idx += 1


    for i in range(start, end + 1):
        src[i] = temp[i]
mergeSort(0, n - 1)

print(src)