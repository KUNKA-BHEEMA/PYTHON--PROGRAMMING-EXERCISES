# Function to simulate XOR Gate
def XOR(A, B):
	return A ^ B

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

# Function to simulate XNOR Gate
def XNOR(A, B):
	return NOT(XOR(A, B))


print("Output of 0 XNOR 0 is", XNOR(0, 0))
print("Output of 0 XNOR 1 is", XNOR(0, 1))
print("Output of 1 XNOR 0 is", XNOR(1, 0))
print("Output of 1 XNOR 1 is", XNOR(1, 1))

