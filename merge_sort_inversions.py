def inversions(items):
    n = len(items)
    if n <= 1:
        return items, 0
    # number of inversions in partitions
    left, linv = inversions(items[:n // 2])
    right, rinv = inversions(items[n // 2:])
    inv = linv + rinv
    llen, rlen = len(left), len(right)
    i, j, aux = 0, 0, []
    # merge and count inversions
    for k in range(n):
        if i < llen and j < rlen and left[i] > right[j]:
            inv += llen - i
            aux.append(right[j])
            j += 1
        elif i < llen:
            aux.append(left[i])
            i += 1
        else:
            aux.append(right[j])
            j += 1
    
    return aux, inv
print([23, 6, 17, 0, 18, 28, 29, 4, 15, 11])
print(inversions([23, 6, 17, 0, 18, 28, 29, 4, 15, 11]))

def mergeSort(items):
    n= len(items)
    if(n <=1):
        return items
    else:
        left = mergeSort(items[:n // 2])
        right = mergeSort(items[n // 2:])
        i =0
        j =0
        aux=[]
        llen,rlen = len(left),len(right)
        for k in range(n):
            if i < llen and j < rlen and left[i] > right[j]:
                aux.append(right[j])
                j += 1
            elif i < llen:
                aux.append(left[i])
                i += 1
            else:
                aux.append(right[j])
                j += 1
    return aux

print(mergeSort([23, 6, 17, 0, 18, 28, 29, 4, 15, 11]))

