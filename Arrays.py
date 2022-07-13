from array import *

arr1 = array('i', [1,2,3,4,5,6])

#insertion at end of arr1
arr1.insert(6, 7)


#insertaion at start of arr1

arr1.insert(0, 0)

#array traversel 
def traverseArray(array):
    for i in array: 
        print(i)

traverseArray(arr1)

#accessing elements

def access(array, index):
    if index > len(array):
        return("There is not any element in this array")
    else:
        return(array[index])

def searchArray(array, value): 
    for i in array: 
        if i == value: 
            return array.index(value)
    return "The element does not exist in this array"
    