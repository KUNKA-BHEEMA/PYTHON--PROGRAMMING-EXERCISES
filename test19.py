'''
Write a program to find common values between two arrays.
Using set( ).intersection(), We can print the list of common elements of a list, but it can not store in any of the variables.
If both lists do not contain any common elements then it will return an empty set( ).
'''


a=[2,9,4,5]
b=[3,5,7,2]
print(set(a).intersection(b))
