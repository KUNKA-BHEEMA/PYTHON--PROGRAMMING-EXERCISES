'''
Implementation of Half-adder
'''
# Function to print sum and carry
def getResult(A, B):

	# Calculating value of sum
	Sum = A ^ B
	
	# Calculating value of Carry
	Carry = A & B
	
	# printing the values
	print("Sum ", Sum)
	print("Carry", Carry)


# Driver code
A = 0
B = 1

# passing two inputs of halfadder as arguments to get result function
getResult(A, B)
