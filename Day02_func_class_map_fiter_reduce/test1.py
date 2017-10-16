def update(list1):
    for i in range(len(list1)):
        list1[i] *= list1[i]
    return list1


list2 = [1, 2, 3, 4, 5]
print list2
print update(list2)
print list2
