def binary_search(haystack, noodle):
	low = 0
	height = len(haystack) - 1

	while low <= height:
		mid = int((low + height)/2)
		if noodle == haystack[mid]:
			return mid
		elif noodle > haystack[mid]:
			low = mid + 1
		else:
			height = mid - 1
			
	return -1