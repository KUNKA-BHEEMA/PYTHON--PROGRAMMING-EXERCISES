'''
Write a function unique to find all the unique elements of a list.
Initially, we will need to convert the input list to set using the set() function.
As the list gets converted to set, only a single copy of all the duplicate elements gets placed into it.
Then, we will have to convert the set back to the list 
'''

list_inp = [100, 75, 100, 20, 75, 12, 75, 25] 

set_res = set(list_inp) 
print("The unique elements of the input list using set():\n") 
list_res = (list(set_res))
 
for item in list_res: 
    print(item)

