def quick_sort(list):

	if len(list) <= 1:
		return list

	check = 0
	pivot = len(list) -1

	while check < pivot:
		if list[check] > list[pivot]:
			holder = list[check]
			list[check] = list[pivot -1]
			list[pivot -1] = list[pivot]
			list[pivot] = holder

			pivot -= 1
		else:
			check += 1
	return quick_sort(list[:pivot]) + [list[pivot]] + quick_sort(list[pivot+1:])