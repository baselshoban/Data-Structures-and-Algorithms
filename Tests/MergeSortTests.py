import sys
sys.path.append("../")

from Algorithms.MergeSort import merge_sort

try:
	print("\nStart Merge Sort Tests ..")

	# Test empty list case
	sorted_list = merge_sort([])
	assert sorted_list == []

	# Test list with odd number of elements
	unsorted_list = [5, 1, 6, 7, 11]
	sorted_list = merge_sort(unsorted_list)
	assert sorted_list == [1, 5, 6, 7, 11]

	# Test list with even number of elements
	unsorted_list = [2, 9, 1, 7]
	sorted_list = merge_sort(unsorted_list)
	assert sorted_list == [1, 2, 7, 9]

	# Test list with negative elements
	unsorted_list = [5, -1, 6, -7, 11]
	sorted_list = merge_sort(unsorted_list)
	assert sorted_list == [-7, -1, 5, 6, 11]

	# Test list with similar elements
	unsorted_list = [12, 5, 12, 6, 0]
	sorted_list = merge_sort(unsorted_list)
	assert sorted_list == [0, 5, 6, 12, 12]

	print("All Tests Pass Successfuly")

except AssertionError as e:
	print("Tests Fails")
except Exception as e:
	print("An Error Accoured")
	raise e