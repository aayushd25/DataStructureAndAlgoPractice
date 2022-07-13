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