def binarySearch(my_array, target):
    left = 0
    right = len(my_array) -1
    result = helper(my_array, target, left, right)
    return result

def helper(my_array, target, left, right):
    if left > right:
        return -1
    middle = (left + right)//2
    middle_element = my_array[middle]

    if target == middle_element:
       return middle
    elif target < middle_element:
       return helper(my_array, target, left, middle-1)
    else:
       return helper(my_array, target, middle+1, right)

print(binarySearch([2,4,5,7,8,9,15,20], 9))

