'''
Write a function unique to find all the unique elements of a list.
Python numpy.unique() function To Create a List with Unique Items
Python NumPy module has a built-in function named, numpy.unique to fetch unique data items from a numpy array.

In order to get unique elements from a Python list, we will need to convert the list to NumPy array using the below command:
Syntax:

numpy.array(list-name)

Next, we will use the numpy.unique() method to fetch the unique data items from the numpy array
and finally, we’ll print the resulting list.
Syntax:

numpy.unique(numpy-array-name


'''

import numpy as N
list_inp = [100, 75, 100, 20, 75, 12, 75, 25] 

res = N.array(list_inp) 
unique_res = N.unique(res) 
print("Unique elements of the list using numpy.unique():\n")
print(unique_res)

