def bubble_sort(list_value):
    lenth = len(list_value)

    for i in range(0, lenth):
        for j in range(0, lenth-i-1):
            if list_value[j] > list_value[j+1]:
                #if first value is greater then 2nd one than swap the value
                list_value[j],list_value[j+1]= list_value[j+1],list_value[j] 


if __name__ == '__main__':
    list_value = [6,1,4,9,2]
    print('Befor sort', list_value)
    bubble_sort(list_value)
    print('After Sort', list_value)
