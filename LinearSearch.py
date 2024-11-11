def linear_search(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1

list = [10,20,30,40,50]
x = 40
result = linear_search(list, x)
print(result)
