import sys
sys.path.append("../")

from Algorithms.BubbleSort import bubble_sort

try:
	print("\nStart Bubble Sort Tests ..")

	# Test empty list 
	sorted_list = bubble_sort([])
	assert sorted_list == []

	# Test list with even number of elements
	sorted_list = bubble_sort([9, 1, 6, 12])
	assert sorted_list == [1, 6, 9, 12]

	# Test list with odd number of elements
	sorted_list = bubble_sort([1, 4, 2, 8, 5])
	assert sorted_list == [1, 2, 4, 5, 8]

	# Test list with negative elements
	sorted_list = bubble_sort([-5, 0, 3, -1, 6])
	assert sorted_list == [-5, -1, 0, 3, 6]

	print("All Tests Pass Successfuly")

except AssertionError as e:
	print("Tests Fail")
except Exception as e:
	print("An Error Accoured")
	raise e
