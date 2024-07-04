# Function to simulate OR Gate
def OR(A, B):
	return A | B	

print("Output of 0 OR 0 is", OR(0, 0))
print("Output of 0 OR 1 is", OR(0, 1))
print("Output of 1 OR 0 is", OR(1, 0))
print("Output of 1 OR 1 is", OR(1, 1))

# Function to simulate AND Gate
def AND(A, B):
	return A & B	

print("Output of 0 AND 0 is", AND(0, 0))
print("Output of 0 AND 1 is", AND(0, 1))
print("Output of 1 AND 0 is", AND(1, 0))
print("Output of 1 AND 1 is", AND(1, 1))


# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

print("Output of NOT 0 is", NOT(0))
print("Output of NOT 1 is", NOT(1))


