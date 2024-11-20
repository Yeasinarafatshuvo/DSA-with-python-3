def selection_sort(arrs):
    n = len(arrs)

    for i in range(0, n-1):
        index_min = i
        for j in range(i+1, n):
            if arrs[j] < arrs[index_min]:
                index_min = j
        if index_min != i:
            arrs[i], arrs[index_min] = arrs[index_min], arrs[i]
    return arrs

arrs = [6,1,4,9,2]
print(selection_sort(arrs))
            
