import sys
sys.path.append("../")

from Algorithms.Recursion import recursion_fibonacci

try:
	print("\nStart Recursion Tests ..")

	# Test cases
	assert recursion_fibonacci(9) == 34
	assert recursion_fibonacci(11) == 89

	# Test base cases
	assert recursion_fibonacci(1) == 1
	assert recursion_fibonacci(0) == 0

	# Test negative cases
	assert recursion_fibonacci(-5) == -1

	print("All Tests Pass Successfuly")

except AssertionError as e:
	print("Tests Fail")
except Exception as e:
	print("An Error Accoured: ")
	raise e