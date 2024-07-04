#Python program to find the GCD of two non-zero numbers
# importing the module
#Give two numbers in the same line separated by blank space
import math

# input two numbers
m,n=map(int,input('Enter two non-zero numbers: ').split())

#to find GCD
g=math.gcd(m,n) 

# printing the result
print('GCD of {} and {} is {}.'.format(m,n,g))

