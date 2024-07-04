'''
Write a program to find common values between two arrays.

Make a function for both lists. If there are common elements in both the list, then it will return common elements in list c.
If both lists do not contain any common elements then it will return an empty list.

'''

a=[2,3,4,5]
b=[3,5,7,9]

def common(a,b): 
    c = [value for value in a if value in b] 
    return c

d=common(a,b)
print(d)
