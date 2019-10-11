def binary_search(haystack, noodle):
	low = 0
	high = len(haystack) - 1

	while low <= high:
		mid = int((low + high)/2)
		if noodle == haystack[mid]:
			return mid
		elif noodle > haystack[mid]:
			low = mid + 1
		else:
			high = mid - 1
			
	return -1