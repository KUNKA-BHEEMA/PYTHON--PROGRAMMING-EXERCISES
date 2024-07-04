#Python program to find the GCD of the array
# importing the module
import math

# array of integers
A=[40,24,56,96]

#initialize variable b as first element of A
b=A[0]  
for j in range(1,len(A)):
    s=math.gcd(b,A[j])
    b=s
print('GCD of array elements is  {}.'.format(b))
