'''
Write a function unique to find all the unique elements of a list.

In order to find the unique elements, we can apply a Python for loop along with list.append() function to achieve the same.
At first, we create a new (empty) list i.e res_list.
After this, using a for loop we check for the presence of a particular element in the new list created (res_list). If the element is not present, it gets added to the new list using the append() method.
In case, we come across an element while traversing that already exists in the new list i.e. a duplicate element, in such case it is neglected by the for loop. We will use the if statement to check whether it’s a unique element or a duplicate one

'''
list_inp = [100, 75, 100, 20, 75, 12, 75, 25] 

res_list = []

for item in list_inp: 
    if item not in res_list: 
        res_list.append(item) 

print("Unique elements of the list using append():\n")    
for item in res_list: 
    print(item)

