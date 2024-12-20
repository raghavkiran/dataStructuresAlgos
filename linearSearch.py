def linearSearch(my_array, target):
    for i in range(len(my_array)):
        if my_array[i] == target:
            return i
    return -1

found = linearSearch([5,3,1,9,2,7], 9)
if found != -1:
    print("search target found in my_array")
else:
    print("Not found")
