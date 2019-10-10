import sys
sys.path.append("../")

from Algorithms.BinarySearch import binary_search

try:
	# Set up a haystack
	test_list = [1,3,9,11,15,19,29]
	test_val1 = 25
	test_val2 = 15

	# Test not found noodle
	assert binary_search(test_list, test_val1) == -1

	# Test exist noodle
	assert binary_search(test_list, test_val2) == 4
	
	print("All Tests Pass Successfuly")

except AssertionError as e:
	print("Tests Fail")
except Exception as e:
	print("An Error Accoured: ")
	raise e