#Remove List Item Using remove() Method
#he remove() method in Python is used to remove the first occurrence of a specified item from a list.

##We can remove list items using the remove() method by specifying the value we want to remove within the parentheses, like my_list.remove(value), which deletes the first occurrence of value from my_list.

#Example
#In the following example, we are deleting the element "Physics" from the list "list1" 
# using the remove() method −

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
list1.remove(21)
print(list1)