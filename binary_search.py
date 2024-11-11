def binarySearchTree(list, x):
    left = 0
    right = len(list) - 1

    while(left <= right):
        mid = (left + right) // 2     #interger division
        if list[mid] == x:
            return mid
        
        if list[mid] < x:
            left = mid + 1
        else:
            right =  mid - 1
    return -1

list = [10,20,30,40,50]
x = 58
result = binarySearchTree(list, x)
print(result)
