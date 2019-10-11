def merge_sort(list):

	# Merge two parts
	def merge(part1, part2):
		i = 0
		j = 0
		merged = []

		while i < len(part1) and j < len(part2):
			if part1[i] < part2[j]:
				merged.append(part1[i])
				i += 1
			elif part2[j] < part1[i]:
				merged.append(part2[j])
				j += 1
			else:
				merged.append(part1[i])
				merged.append(part2[j])
				i += 1
				j += 1

		if i < len(part1):
			merged = merged + part1[i:]
		if j < len(part2):
			merged = merged + part2[j:]

		return merged

	# Divide list into parts
	def divide(list, low, high):
		if high > low:
			mid = int( (low + high) / 2 )
			part1 = divide(list, low, mid)
			part2 = divide(list, mid +1, high)

			return merge(part1, part2)
		return [list[high]]

	# Check if list is empty
	if not list:
		return list
	
	return divide(list, 0, len(list) -1)