'''
Explanation
The list (l) with duplicate elements is taken to find the duplicates.

An empty list (l1) is taken to store the values of non-duplicate elements from the given list.

The for loop is used to access the values in the list (l), and the if condition is used to check if the elements in the given list (l) are present in the empty list (l1).

If the elements are not present, those values are appended to the list (l1); else, they are printed.

Here, the list (l1) has no duplicates. The values printed are the duplicates from list (l).
'''
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

