from array import * 

#1. create array and traverse through array

arr = array('i', [1,2,3,4,5])

for i in range(len(arr)):
    print(arr[i])

#2. accessing elements via indexes 
print("Step 2")
print(arr[0])

#3. use append to add to element
print("Step 3")
arr.append(6)

#4. insert value using insert() method 
print("Step 4")
arr.insert(3, 11)
print(arr)

#5. extend python array using extend() method 
print("Step 5")
arr1 = array('i', [10, 11, 12])
arr.extend(arr1)
print(arr)

#6. fromlist() method to add items from list to array
print("Step 6")
list = [20, 21, 22]
arr.fromlist(list)
print(arr)

#7. remove element using remove() method 
print("Step 7")
arr.remove(11)
print(arr)

#8. remove last element using pop() method 
print("Step 8")
arr.pop()
print(arr)

#9. fetch element using index() method 
print("Step 9")
print(arr.index(21))

#10. reverse array using reverse() method 
print("Step 10")
arr.reverse()
print(arr)

#11. get array buffer info from buffer_info() method 
print("Step 11")
print(arr.buffer_info())

#12. check for number of occurrences using count() method 
print("Step 12")
arr.append(11)
print(arr.count(11))

#13. convert arry to list
print("Step 13")
print(arr.tolist())

#14. slice elements from array
print("Step 14")
print(arr[0:3])