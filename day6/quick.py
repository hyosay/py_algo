''''src  = [2, 3, 4, 1, 5, 6, 7, 8]
n = len(src)

def quickSort(s, e):
    if s < e:
        p = s
        l = s
        r = e

        while  l <= r:
            while src[p] >= src[l] and l < e:
                l += 1
            while src[p] < src[r]:
                r -= 1
            if l <= r:
                src[l], src[r] = src[r], src[l]
        src[r] , src[p] = src[p], src[r]

        quickSort(s, r -1)
        quickSort(r + 1, e)
quickSort(0, n- 1 )
print(src)'''


a = list(range(1, 1000))
print(a)