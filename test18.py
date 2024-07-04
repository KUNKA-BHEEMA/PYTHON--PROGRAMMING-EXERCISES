'''
Write a program to find common values between two arrays.
Using set( ) function, We can return common elements of a list in the third variable.  If both lists do not contain any common elements then it will return an empty list.
'''

a=[2,9,4,5]
b=[3,5,7,9]
def common(lst1, lst2): 
    return list(set(lst1) & set(lst2))
e=common(a,b)
print(e)
